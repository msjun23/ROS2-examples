import rclpy
import my_controller.comm as comm

import cv2

def main():
    rclpy.init(args=None)
    my_controller_publisher = comm.ClientPublisher()
    my_controller_subscriber = comm.ClientSubscriber()
    
    # rclpy.spin(my_controller_publisher)
    rclpy.spin_once(my_controller_subscriber)
    
    my_img = my_controller_subscriber.GetImage()
    cv2.imshow('My img', my_img)
    cv2.waitKey(0)
    
    my_controller_publisher.destroy_node()
    my_controller_subscriber.destroy_node()
    rclpy.shutdown

if __name__ == '__main__':
    main()
