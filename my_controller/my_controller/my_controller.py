import rclpy
import my_controller.comm as comm

import cv2

def main():
    rclpy.init(args=None)
    
    my_controller_publisher = comm.ClientPublisher()
    my_controller_subscriber = comm.ClientSubscriber()
    
    while True:
        rclpy.spin_once(my_controller_publisher)
        rclpy.spin_once(my_controller_subscriber)
        
        my_img = my_controller_subscriber.GetImage()
        my_img = cv2.resize(my_img, dsize=(640, 480), interpolation=cv2.INTER_AREA)
        cv2.imshow('My img', my_img)
        keyin = cv2.waitKey(1)  # Wait for key 1 second
        if (keyin == ord('w')):
            my_controller_publisher.set_velocity(0.1, 0.0)
        elif (keyin == ord('a')):
            my_controller_publisher.set_velocity(0.0, 0.1)
        elif (keyin == ord('d')):
            my_controller_publisher.set_velocity(0.0, -0.1)
        elif (keyin == ord('s')):
            my_controller_publisher.set_velocity(-0.1, 0.0)
        elif (keyin == ord('q')):
            my_controller_publisher.set_velocity(0.1, 0.1)
        elif (keyin == ord('e')):
            my_controller_publisher.set_velocity(0.1, -0.1)
        elif (keyin == 32):     # Space bar
            my_controller_publisher.set_velocity(0.0, 0.0)
        elif (keyin == ord('f')):
            break
    
    my_controller_publisher.destroy_node()
    my_controller_subscriber.destroy_node()
    rclpy.shutdown

if __name__ == '__main__':
    main()
