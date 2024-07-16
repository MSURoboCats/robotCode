import rclpy
from rclpy.node import Node

from interfaces.msg import ControlData, HullData

from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import BatteryState, Image

import pygame
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageTk
from PIL import Image as PILImage
from threading import Thread
import time

from cv_bridge import CvBridge
import cv2

global vel
vel = 1

def EX_button_on(num):
    print("ON %f" % num)

def EX_button_off(num):
    print("OFF %f" % num)

#this is just to save space with all of the buttons I was making
# it makes a on/off button if you dont want this just set the off and on backgrounds and funcs to the same things
class button():
    def __init__(self,tab,name, grid_pos, off_func, on_func, off_background, on_background,args = "none"):
        self.on = on_func; self.off = off_func; self.args = args
        self.back = [off_background,on_background]
        self.idx = 0
        self.btn = tk.Button(tab,text = name, command = self.switch,bg = self.back[self.idx])
        self.btn.grid(**grid_pos)
    def switch(self):
        if self.idx == 0:
            self.idx =1
            if self.args != "none":
                self.on(self.args)
            else:
                self.on()
        else:
            self.idx = 0
            if self.args != "none":
                self.off(self.args)
            else:
                self.off()
        self.btn.configure(bg=self.back[self.idx])

class MotorChooser():
    def __init__(self, tab, motor_num, row, col_start):
       label_text = "Motor "+str(motor_num)+")    "
       ttk.Label(tab, text =label_text, font = "Helvetica 10 bold").grid(column = col_start, row = row)
       ESCs = ["1", "2", "3","4","5","6","7","8"]; directions = ["Forward","Reverse"]
       ESC = tk.StringVar(tab);ESC.set("Choose ESC"); direction = tk.StringVar(tab); direction.set("Choose Direction")
       drop_ESC = tk.OptionMenu(tab ,ESC , *ESCs ); drop_dir = tk.OptionMenu(tab, direction, *directions)
       
       ttk.Label(tab, text ="ESC: ").grid(column = col_start+1, row = row);drop_ESC.grid(column = col_start+2, row=row)
       ttk.Label(tab, text ="Direction: ").grid(column = col_start+3, row = row);drop_dir.grid(column = col_start+4, row =row)

class GUI():
    def __init__(self):
        #makes tabs and sets up titles
        print("initializing GUI")
        self.paddings = {'padx': 5, 'pady': 5}
        self.root = tk.Tk()
        self.savePath = tk.StringVar()
        self.root.geometry("1000x1000")
        self.root.title("ROBOCATS SUB CONTROL NODE")
        self.SubControlNode = ttk.Notebook(self.root)  
        self.motorMappings()
        self.options()

        self.SubControlNode.pack(expand = 1, fill ="both")

        rclpy.init()
        self.ros_node = AllKnowingNode(self)
    
    def start(self):
        self.root.mainloop()

    def motorMappings(self):
       
        MM = tk.Frame(self.SubControlNode)
       
        self.SubControlNode.add(MM, text ='Motor Mappings')
        ttk.Label(MM, text ="Motor Mappings: ", font = "Helvetica 12 bold").grid(column = 0, row = 0,  **self.paddings)

        #image showing
        image = PILImage.open("SUB-PICTURE.png")
        canvas_for_motor_mappings = tk.Canvas(MM, bg='green', height=348, width=438, borderwidth=0, highlightthickness=0)
        canvas_for_motor_mappings.grid(row=1, column=0, sticky='nesw', padx=0, pady=0,rowspan = 16)
        canvas_for_motor_mappings.image = ImageTk.PhotoImage(image.resize((438, 348)))
        canvas_for_motor_mappings.create_image(0, 0, image=canvas_for_motor_mappings.image, anchor='nw')
       
        self.M1 = MotorChooser(MM,1,1,1)
        self.M2 = MotorChooser(MM,2,3,1)
        self.M3 = MotorChooser(MM,3,5,1)
        self.M4 = MotorChooser(MM,4,7,1)
        self.M5 = MotorChooser(MM,5,9,1)
        self.M6 = MotorChooser(MM,6,11,1)
        self.M7 = MotorChooser(MM,7,13,1)
        self.M8 = MotorChooser(MM,8,15,1)
       
        ttk.Label(MM, text ="Test ESC: ").grid(column = 2, row = 17,  **self.paddings)
        ESCs = [1,2,3,4,5,6,7,8]; ESC = tk.IntVar(MM); ESC.set(1);
        drop_ESC = tk.OptionMenu(MM ,ESC , *ESCs, );drop_ESC.grid(column = 3, row=17)
        button(MM,"Test", {'row':17,'column':4}, lambda *args: self.ros_node.get_logger().info(str(ESC.get())), lambda *args: self.ros_node.get_logger().info(str(ESC.get())),"grey","grey")
   
    #all of the options
    def options(self):
        #sets up tabs
        Options = ttk.Frame(self.SubControlNode)
        self.SubControlNode.add(Options, text ='Options')
        ttk.Label(Options, text ="Image Collection: ").grid(column = 0, row = 0,  **self.paddings)
       
        #image collection buttons
        ttk.Label(Options, text ="Cameras: ").grid(column = 0, row = 1,  **self.paddings)
        forward = button(Options,"FORWARD", {'row':1,'column':1}, lambda: setattr(self.ros_node, 'forward_feed', False), lambda: setattr(self.ros_node, 'forward_feed', True),"grey","green")
        down = button(Options,"DOWN", {'row':1,'column':2}, EX_button_off,EX_button_on,"grey","green")
        #stereo = button(Options,"STEREO", {'row':1,'column':4}, EX_button_off,EX_button_on,"grey","green")

       
        #image collection file path chooser
        ttk.Label(Options, text ="Path To Save: ").grid(column = 0, row = 2,  **self.paddings)
        self.path_entry = ttk.Entry(Options, textvariable=self.savePath)
        self.path_entry.insert(0, '/home/robocats/Desktop/developmentEnvironment/robotCode/competitionCode2024/ros2_ws/training_data')
        self.path_entry.grid(column = 1,row =2, **self.paddings)
        button(Options,"Search Path", {'row':2,'column':2}, self.browsefunc,self.browsefunc,"grey","grey")

        #Image collection folder name
        ttk.Label(Options, text ="Folder name: ").grid(column = 0, row = 3,  **self.paddings)
        self.training_data_folder_name = tk.StringVar()
        intervalTextbox = ttk.Entry(Options, textvariable=self.training_data_folder_name)
        intervalTextbox.insert(0, 'test1')
        intervalTextbox.grid(column = 1, row = 3, **self.paddings)
        intervalTextbox.focus()

        #Image collection saving interval
        ttk.Label(Options, text ="Saving Interval (seconds): ").grid(column = 0, row = 4,  **self.paddings)
        self.interval = tk.StringVar()
        intervalTextbox = ttk.Entry(Options, textvariable=self.interval)
        intervalTextbox.insert(0, '1')
        intervalTextbox.grid(column = 1, row = 4, **self.paddings)
        intervalTextbox.focus()
        
        #live preview has drop down menu and a button to launch it
        cameras = ["FORWARD", "", ""]; CVModels = ["pool_tuned_base","dry_buoy"]
        cam = tk.StringVar(Options);cam.set("Choose Camera"); mod = tk.StringVar(Options); mod.set("Choose CV Model")
        drop_cam = tk.OptionMenu( Options ,cam , *cameras ); drop_mod = tk.OptionMenu(Options, mod, *CVModels)
        drop_cam.grid(column = 0, row=5); drop_mod.grid(column = 1, row =5)
        Live_btn = button(Options,"Launch live", {'row':5,'column':2}, EX_button_off,EX_button_on,"grey","grey")

        # built-in live preview:
        self.canvas_for_live_preview_1 = tk.Canvas(Options, bg='green', height=348, width=438, borderwidth=0, highlightthickness=0)
        self.canvas_for_live_preview_1.grid(row=0, column=3, sticky='nesw', padx=0, pady=0,rowspan = 16)
       
        self.battery_level = tk.StringVar()
        self.temp = tk.StringVar()
        self.pressure = tk.StringVar()
        self.humidity = tk.StringVar()
        self.depth = tk.StringVar()
        self.rot = tk.StringVar()
        self.rot_vel = tk.StringVar()
        self.lin_acc= tk.StringVar()
        #how you can set variables ex) self.battery_level.set(str(90)))
        #this just shows the status
        ttk.Label(Options, text ="Sub status: ").grid(column = 0, row = 7,  **self.paddings)
        ttk.Label(Options, text = "Battery Level:").grid(column = 0, row = 8,  **self.paddings);ttk.Label(Options, textvariable = self.battery_level).grid(column = 1, row = 7,  **self.paddings)
        ttk.Label(Options, text = "Tempature:").grid(column = 2, row = 8,  **self.paddings);ttk.Label(Options, textvariable = self.temp).grid(column = 3, row = 7,  **self.paddings)
        ttk.Label(Options, text = "Pressure:").grid(column = 0, row = 9,  **self.paddings);ttk.Label(Options, textvariable = self.pressure).grid(column = 1, row = 8,  **self.paddings)
        ttk.Label(Options, text = "Humidity:").grid(column = 2, row = 9,  **self.paddings);ttk.Label(Options, textvariable = self.humidity).grid(column = 3, row = 8,  **self.paddings)
        ttk.Label(Options, text = "Depth:").grid(column = 0, row = 10,  **self.paddings);ttk.Label(Options, textvariable = self.depth).grid(column = 1, row = 9,  **self.paddings)
        ttk.Label(Options, text = "Rot:").grid(column = 2, row = 10,  **self.paddings);ttk.Label(Options, textvariable = self.rot).grid(column = 3, row = 9,  **self.paddings)
        ttk.Label(Options, text = "Angular Velocity:").grid(column = 0, row = 11,  **self.paddings);ttk.Label(Options, textvariable = self.rot_vel).grid(column = 1, row = 10,  **self.paddings)
        ttk.Label(Options, text = "Linear Acceleration:").grid(column = 2, row = 11,  **self.paddings);ttk.Label(Options, textvariable = self.lin_acc).grid(column = 3, row = 10,  **self.paddings)
       
        #sub controller
        slider_label = ttk.Label(Options,text='Motor Controler:')
        slider_label.grid(column=0, row=12,sticky='w')
        self.current_value = tk.DoubleVar()
        slider = ttk.Scale(Options,from_=0,to=100,orient='horizontal', command=self.slider_changed, variable=self.current_value)
        slider.grid(column=1,row=13,sticky='we')
        current_value_label = ttk.Label( Options,text='Motor power percentage:')
        current_value_label.grid(row=14, column=1, sticky='n',ipadx=10, ipady=10)
        # value label
        val = self.get_current_value()
        self.value_label = ttk.Label(Options, text=val)
        self.value_label.grid(row=15,column=2,sticky='n')
       
        controller_btn = button(Options,"Launch Controller", {'row':15,'column':2}, self.open_controller,self.open_controller,"grey","grey")

        button(Options,"ABORT", {'row':16,'column':0}, EX_button_off,EX_button_off,"red","red")

    def open_controller(self):
       pass

    def get_current_value(self):
        global vel
        val = self.current_value.get()
        vel = val / 100.0
        return('{: .2f}'.format(val))

    def slider_changed(self,event):
        global vel
        vel = self.get_current_value()
        vel = float(vel)
        self.value_label.configure(text=self.get_current_value())
   
    def browsefunc(self):
        filename =filedialog.askdirectory()
        self.path_entry.insert(tk.END, filename) # add this
    
    def start_ros(self):
        rclpy.spin(self.ros_node)

def GUI_launch():
    global gui
    gui = GUI()
    p = Thread(target=gui.start_ros)
    p.start()
    gui.start()

class AllKnowingNode(Node):

    def __init__(self, gui: GUI):
        super().__init__("all_knowing_gui_node")

        # publisher for twists to control the sub
        self.pub_control_twist = self.create_publisher(
            Twist,
            "control_twist",
            10,
        )

        # publisher for controlling/starting/stopping frame saver
        self.pub_frame_saver = self.create_publisher(
            String,
            "/frame_saver_commands",
            10,
        )

        # subscriber for control data
        self.sub_control_data = self.create_subscription(
            ControlData,
            '/control_data',
            self.control_data_callback,
            10,
        )

        # subscriber for hull data
        self.sub_control_data = self.create_subscription(
            HullData,
            '/hull_data',
            self.hull_data_callback,
            10,
        )

        # subscriber for voltage
        self.voltage = self.create_subscription(
            BatteryState,
            'battery_health',
            self.voltage_callback,
            10,
        )

        # subscriber for forward camera
        self.sub_forward_rgb_camera = self.create_subscription(
            Image, 
            '/forward_rgb_camera/video_frames', 
            self.sub_forward_rgb_camera_callback, 
            10
        )
        
        # subscriber for downward camera
        self.sub_forward_rgb_camera = self.create_subscription(
            Image, 
            '/downard_rgb_camera/video_frames', 
            self.sub_downward_rgb_camera_callback, 
            10
        )

        # timer for saving images
        self.save_timer = self.create_timer(10, self.save_callback)
        self.save_timer.timer_period_ns = 1000000000*self.save_timer_period

        self.br = CvBridge()

        self.forward_feed = False
        self.downward_feed = False
        self.save_feed = False

        self.gui = gui

    def control_data_callback(self, data: ControlData) -> None:
        self.gui.depth.set(str(data.depth))
    
    def hull_data_callback(self, data: HullData) -> None:
        self.gui.temp.set(str(data.temperature.temperature))
        self.gui.pressure.set(str(data.pressure.fluid_pressure))
        self.gui.humidity.set(str(data.humidity.relative_humidity))
    
    def voltage_callback(self, data: BatteryState) -> None:
        self.gui.battery_level.set(str(data.voltage))

    def sub_forward_rgb_camera_callback(self, data: Image) -> None:
        if self.forward_feed:
            # convert to cv2 format and display
            current_frame = self.br.imgmsg_to_cv2(data)
            b, g, r = cv2.split(current_frame)
            adjusted_frame = PILImage.fromarray(cv2.merge((r,g,b)))
            self.gui.canvas_for_live_preview_1.image = ImageTk.PhotoImage(adjusted_frame)
            self.gui.canvas_for_live_preview_1.create_image(0, 0, image=self.gui.canvas_for_live_preview_1.image, anchor='nw')

    def sub_downward_rgb_camera_callback(self, data: Image) -> None:
        if self.downward_feed:
            # convert to cv2 format and display
            pass
            '''
            need to add into GUI
            current_frame = self.br.imgmsg_to_cv2(data)
            b, g, r = cv2.split(current_frame)
            adjusted_frame = PILImage.fromarray(cv2.merge((r,g,b)))
            self.gui.canvas_for_live_preview_2.image = ImageTk.PhotoImage(adjusted_frame)
            self.gui.canvas_for_live_preview_2.create_image(0, 0, image=self.gui.canvas_for_live_preview_1.image, anchor='nw')
            '''

    def save_callback(self) -> None:
        if self.save_feed:
            print("saved(fake)")
            '''
            # ensure that a frame has been received before trying to save images
            if type(self.frame) == np.ndarray:
                cv2.imwrite(full_img_path, self.frame)
                self.get_logger().info("Frame saved: %s" % ('cv_training_data/' + str(sys.argv[1]) + '/' + str(self.counter) + '.jpg'))
                self.counter += 1
            else:
                self.get_logger().info("Frame lock not aquired")
            '''

def spin_listener(args = None):

    # initialize the rclpy library
    rclpy.init(args=args)

    # create the node
    node = AllKnowingNode()

    # spin the node so the callback function is called
    rclpy.spin(node)

    # destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
  
    # shutdown the ROS client library for Python
    rclpy.shutdown()

def main(args=None):
    GUI_launch()

if __name__ == "__main__":
    main()
