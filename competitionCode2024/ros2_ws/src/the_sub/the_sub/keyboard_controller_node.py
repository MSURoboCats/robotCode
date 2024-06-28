import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

import pygame

class KeyboardController(Node):

    def __init__(self):
        super().__init__("KeuboardController")

        # publisher for twists to control the sub
        self.twist_pub = self.create_publisher(Twist, "control_twist", 10)
        
        # pygame setup
        pygame.init()
        window = pygame.display.set_mode((300, 300))
        clock = pygame.time.Clock()
        rect = pygame.Rect(0, 0, 20, 20)
        rect.center = window.get_rect().center
        keyboard_twist = 5
        run = True

        # keep track of last command
        pre_move = [0,0,0]
        pre_rot = [0,0]
        keyboard_twist = Twist()

        while run:
            clock.tick(15)#fps

            for event in pygame.event.get():
                # close window
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()
            
            # calculate movement vectors:
            #   l/r arrows for x
            #   up/down arrows for z
            #   w/s keys for y
            #   a/d keys for rotation about y
            move_vec = [keys[pygame.K_RIGHT] - keys[pygame.K_LEFT],
                        keys[pygame.K_w] - keys[pygame.K_s],
                        keys[pygame.K_UP] - keys[pygame.K_DOWN],
                        ]
            rot_vec = [0,
                       keys[pygame.K_a] - keys[pygame.K_d],
                       0,
                       ]
            keyboard_twist.linear.x = float(move_vec[0])
            keyboard_twist.linear.y = float(move_vec[1])
            keyboard_twist.linear.z = float(move_vec[2])
            keyboard_twist.angular.x = float(rot_vec[0])
            keyboard_twist.angular.y = float(rot_vec[1])
            keyboard_twist.angular.z = float(rot_vec[2])

            # update square location
            rect.x += move_vec[0] * keyboard_twist
            rect.y += move_vec[1] * -keyboard_twist
            
            # only publish and upadate previous command when keyboard input changes
            if move_vec != pre_move or rot_vec != pre_rot:
                self.twist_pub.publish(keyboard_twist)
                pre_move = move_vec
                pre_rot = rot_vec

            # update window
            rect.centerx = rect.centerx % window.get_width()
            rect.centery = rect.centery % window.get_height()
            window.fill(0)
            pygame.draw.rect(window, (255, 0, 0), rect)
            pygame.display.flip()

        pygame.quit()

        exit()

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

if __name__ == '__main__':
  main()