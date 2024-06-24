import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

import pygame

class KeyboardController(Node):
    def __init__(self):
        VEL = Twist()
        super().__init__("KeuboardController")
        self.vel_pub = self.create_publisher(Twist, "keyboard_control_twist",10)
        pre_move = [0,0,0]
        pre_rot = [0,0]
        pygame.init()
        window = pygame.display.set_mode((300, 300))
        clock = pygame.time.Clock()

        rect = pygame.Rect(0, 0, 20, 20)
        rect.center = window.get_rect().center
        vel = 5

        run = True
        while run:
            clock.tick(15)#fps
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                

            keys = pygame.key.get_pressed()
            
            
            move_vec = [keys[pygame.K_RIGHT] - keys[pygame.K_LEFT],keys[pygame.K_UP] - keys[pygame.K_DOWN],keys[pygame.K_o]-keys[pygame.K_l]]
            rot_vec = [keys[pygame.K_d] - keys[pygame.K_a],keys[pygame.K_w] - keys[pygame.K_s]]
            VEL.linear.x = float(move_vec[0]); VEL.linear.y=float(move_vec[1]);VEL.linear.z=float(move_vec[2])
            VEL.angular.x = float(rot_vec[0]); VEL.angular.y = float(rot_vec[1])

            rect.x += move_vec[0] * vel
            rect.y += move_vec[1] * -vel
            
            if move_vec != pre_move or rot_vec != pre_rot:
                #print("move vector:",move_vec)
                #print("rotation vector:", rot_vec)
                self.vel_pub.publish(VEL)

            pre_move = move_vec; pre_rot = rot_vec
            rect.centerx = rect.centerx % window.get_width()
            rect.centery = rect.centery % window.get_height()

            window.fill(0)
            pygame.draw.rect(window, (255, 0, 0), rect)
            pygame.display.flip()

        pygame.quit()
        exit()

def main(args = None):
    rclpy.init(args=args)
    node = KeyboardController()
    rclpy.spin(node)
    rclpy.shutdown()


main()