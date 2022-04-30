import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ClientPublisher(Node):
    def __init__(self):
        super().__init__('client_publisher')
        self.publisher = self.create_publisher(String, 'client2server', 10)
        
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        
    def timer_callback(self):
        msg = String()
        msg.data = 'Hello Server! %d' % self.i
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: %s' % msg.data)
        self.i += 1
        
class ClientSubscriber(Node):
    def __init__(self):
        super().__init__('client_subscriber')
        self.subscriber = self.create_subscription(String, 'server2client', self.listener_callback, 10)
        
    def listener_callback(self, msg):
        self.get_logger().info('Subscribed: %s' % msg.data)
        