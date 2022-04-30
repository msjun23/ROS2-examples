import rclpy
import ros2server.comm as comm

def main(args=None):
    rclpy.init(args=args)
    print("Server Run!")
    server_subscriber = comm.ServerSubscriber()
    
    rclpy.spin(server_subscriber)
    server_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
