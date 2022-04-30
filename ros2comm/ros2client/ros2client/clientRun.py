import rclpy
import ros2client.comm as comm

def main(args=None):
    rclpy.init(args=args)
    client_publihser = comm.ClientPublisher()
    
    rclpy.spin(client_publihser)
    client_publihser.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
