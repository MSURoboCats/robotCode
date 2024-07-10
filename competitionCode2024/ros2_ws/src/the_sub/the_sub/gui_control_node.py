import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from sensor_msgs.msg import BatteryState

from interfaces.msg import ControlData, HullData

import pygame
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
from multiprocessing import Process

global vel
vel = 1.0

global global_root; global_root = tk.Tk()
#sub status vars
global battery_level; battery_level = tk.StringVar()
global temp; temp = tk.StringVar()
global pressure; pressure = tk.StringVar()
global humidity; humidity = tk.StringVar()
global depth; depth = tk.StringVar()
global rot; rot = tk.StringVar()
global rot_vel; rot_vel = tk.StringVar()
global lin_acc; lin_acc= tk.StringVar()

def EX_button_on():
    print("ON")

def EX_button_off():
    print("OFF")


class controler():
    def __init__(self):
        global vel
        pre_move = [0,0,0]
        pre_rot = [0,0]
        pygame.init()
        window = pygame.display.set_mode((300, 300))
        clock = pygame.time.Clock()

        rect = pygame.Rect(0, 0, 20, 20)
        rect.center = window.get_rect().center
       

        run = True
        while run:
            clock.tick(15)#fps
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
               

            keys = pygame.key.get_pressed()
           
           
            move_vec = [vel * val for val in [keys[pygame.K_RIGHT] - keys[pygame.K_LEFT],keys[pygame.K_UP] - keys[pygame.K_DOWN],keys[pygame.K_o]-keys[pygame.K_l]]]
            rot_vec = [vel * val for val in [keys[pygame.K_d] - keys[pygame.K_a],keys[pygame.K_w] - keys[pygame.K_s]]]

            rect.x += move_vec[0]
            rect.y += move_vec[1]
           
            if move_vec != pre_move or rot_vec != pre_rot:
                print("move vector:",move_vec)
                print("rotation vector:", rot_vec)

            pre_move = move_vec; pre_rot = rot_vec
            rect.centerx = rect.centerx % window.get_width()
            rect.centery = rect.centery % window.get_height()

            window.fill(0)
            pygame.draw.rect(window, (255, 0, 0), rect)
            pygame.display.flip()

        pygame.quit()

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

class GUI():
    def __init__(self):
        #makes tabs and sets up titles
        print("initializing GUI")
        global global_root
        self.paddings = {'padx': 5, 'pady': 5}
        self.root = global_root
        self.savePath = tk.StringVar()
        self.root.geometry("1000x1000")
        self.root.title("ROBOCATS SUB CONTROL NODE")
        self.SubControlNode = ttk.Notebook(self.root)  
        self.motorMappings()
        self.options()

           
        self.SubControlNode.pack(expand = 1, fill ="both")
        self.root.mainloop()
       
    def motorMappings(self):
        #still having a little trouble with the image so this is incomplete for right now
        MM = ttk.Frame(self.SubControlNode)
        self.SubControlNode.add(MM, text ='Motor Mappings')
        ttk.Label(MM, text ="Motors: ").grid(column = 0, row = 0,  **self.paddings)
        """
        imgDIR = os.getcwd()+"\SUB-PICTURE.png"
        canvas = tk.Canvas(MM, width=600, height=400, bg='white')
        canvas.grid(column = 1, row = 1,  **self.paddings)
        python_image = tk.PhotoImage(master = MM,file=imgDIR)
        canvas.create_image((600, 400),image=python_image)
        """
   
    #all of the options
    def options(self):
        #sets up tabs
        Options = ttk.Frame(self.SubControlNode)
        self.SubControlNode.add(Options, text ='Options')
        ttk.Label(Options, text ="Image Collection: ").grid(column = 0, row = 0,  **self.paddings)
       
        #image collection buttons
        ttk.Label(Options, text ="Cameras: ").grid(column = 1, row = 1,  **self.paddings)
        down = button(Options,"DOWN", {'row':1,'column':2}, EX_button_off,EX_button_on,"grey","green")
        forward = button(Options,"FORWARD", {'row':1,'column':3}, EX_button_off,EX_button_on,"grey","green")
        stereo = button(Options,"STEREO", {'row':1,'column':4}, EX_button_off,EX_button_on,"grey","green")

       
        #image collection file path chooser
        ttk.Label(Options, text ="Path To Save: ").grid(column = 1, row = 2,  **self.paddings)
        self.path_entry = ttk.Entry(Options, textvariable=self.savePath)
        self.path_entry.grid(column = 2,row =2, **self.paddings)
        button(Options,"Search Path", {'row':2,'column':3}, self.browsefunc,self.browsefunc,"grey","grey")
       
        #Image collection saving interval
        ttk.Label(Options, text ="Saving Interval: ").grid(column = 1, row = 3,  **self.paddings)
        self.interval = tk.StringVar()
        intervalTextbox = ttk.Entry(Options, textvariable=self.interval)
        intervalTextbox.grid(column = 2, row = 3, **self.paddings)
        intervalTextbox.focus()
       
        #live preview has drop down menu and a button to launch it
        ttk.Label(Options, text ="Live Preview: ").grid(column = 0, row = 4,  **self.paddings)
        cameras = ["cam1", "cam2", "cam3"]; CVModels = ["mod1","mod2"]
        cam = tk.StringVar(Options);cam.set("Choose Camera"); mod = tk.StringVar(Options); mod.set("Choose CV Model")
        drop_cam = tk.OptionMenu( Options ,cam , *cameras ); drop_mod = tk.OptionMenu(Options, mod, *CVModels)
        drop_cam.grid(column = 1, row=5); drop_mod.grid(column = 2, row =5)
        Live_btn = button(Options,"Launch live", {'row':5,'column':3}, EX_button_off,EX_button_on,"grey","grey")
       

        #how you can set variables ex) self.battery_level.set(str(90)))
        #this just shows the status
        global battery_level, temp, pressure, humidity, depth, rot, rot_vel, lin_acc
        ttk.Label(Options, text ="Sub status: ").grid(column = 0, row = 6,  **self.paddings)
        ttk.Label(Options, text = "Battery Level:").grid(column = 1, row = 7,  **self.paddings);ttk.Label(Options, textvariable = self.battery_level).grid(column = 2, row = 7,  **self.paddings)
        ttk.Label(Options, text = "Tempature:").grid(column = 3, row = 7,  **self.paddings);ttk.Label(Options, textvariable = self.temp).grid(column = 4, row = 7,  **self.paddings)
        ttk.Label(Options, text = "Pressure:").grid(column = 1, row = 8,  **self.paddings);ttk.Label(Options, textvariable = self.pressure).grid(column = 2, row = 8,  **self.paddings)
        ttk.Label(Options, text = "Humidity:").grid(column = 3, row = 8,  **self.paddings);ttk.Label(Options, textvariable = self.humidity).grid(column = 4, row = 8,  **self.paddings)
        ttk.Label(Options, text = "Depth:").grid(column = 1, row = 9,  **self.paddings);ttk.Label(Options, textvariable = self.depth).grid(column = 2, row = 9,  **self.paddings)
        ttk.Label(Options, text = "Rot:").grid(column = 3, row = 9,  **self.paddings);ttk.Label(Options, textvariable = self.rot).grid(column = 4, row = 9,  **self.paddings)
        ttk.Label(Options, text = "Angular Velocity:").grid(column = 1, row = 10,  **self.paddings);ttk.Label(Options, textvariable = self.rot_vel).grid(column = 2, row = 10,  **self.paddings)
        ttk.Label(Options, text = "Linear Acceleration:").grid(column = 3, row = 10,  **self.paddings);ttk.Label(Options, textvariable = self.lin_acc).grid(column = 4, row = 10,  **self.paddings)
       
        #sub controller
        slider_label = ttk.Label(Options,text='Motor Controler:')
        slider_label.grid(column=0, row=11,sticky='w')
        self.current_value = tk.DoubleVar()
        slider = ttk.Scale(Options,from_=0,to=100,orient='horizontal', command=self.slider_changed, variable=self.current_value)
        slider.grid(column=1,row=12,sticky='we')
        current_value_label = ttk.Label( Options,text='Motor power percentage:')
        current_value_label.grid(row=13, column=1, sticky='n',ipadx=10, ipady=10)
        # value label
        val = self.get_current_value()
        self.value_label = ttk.Label(Options, text=val)
        self.value_label.grid(row=13,column=2,sticky='n')
       
        controller_btn = button(Options,"Launch Controller", {'row':14,'column':2}, self.open_controller,self.open_controller,"grey","grey")
       
    def open_controller(self):
       
        pygame_controller = controler()
       
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

def GUI_launch():
    global gui
    gui = GUI()

class KeyboardController(Node):

    def __init__(self):
        super().__init__("KeuboardController")

        # publisher for twists to control the sub
        #self.twist_pub = self.create_publisher(Twist, "control_twist", 10)

        # subscriber for control data
        self.sub_control_data = self.create_subscription(ControlData, '/control_data', self.control_data_callback, 10)

        # subscriber for hull data
        self.sub_control_data = self.create_subscription(HullData, '/hull_data', self.hull_data_callback, 10)

        # subscriber for voltage
        self.voltage = self.create_subscription(BatteryState, "battery_health", self.voltage_callback, 10)

        # subscriber for forward camera

        # subscriber for downward camera
    
    def control_data_callback(self, data: ControlData) -> None:
        global depth, rot, rot_vel, lin_acc
        depth.set(str(data.depth))
    
    def hull_data_callback(self, data: HullData) -> None:
        global tryemp, pressure, humidity
        temp.set(str(data.temperature.temperature))
        pressure.set(str(data.pressure.fluid_pressure))
        humidity.set(str(data.humidity.relative_humidity))
    
    def voltage_callback(self, data: BatteryState) -> None:
        global battery_level
        battery_level.set(str(data.voltage))



def main(args = None):

    # initialize the rclpy library
    rclpy.init(args=args)

    # create the node
    node = KeyboardController()

    # spin the node so the callback function is called
    rclpy.spin(node)

    # destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
  
    # shutdown the ROS client library for Python
    rclpy.shutdown()

print("made it here")
p = Process(target=GUI_launch)
p.start()
print("made it here")
main()
print("made it here")