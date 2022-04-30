import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ServerPublisher(Node):
    def __init__(self):
        super().__init__('server_publisher')
        self.publisher = self.create_publisher(String, 'server2client', 10)
        
    def MessagePublish(self, sendMsg):
        msg = String()
        msg.data = sendMsg
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: %s' % msg.data)
        
class ServerSubscriber(Node):
    def __init__(self):
        super().__init__('server_subscriber')
        self.subscriber = self.create_subscription(String, 'client2server', self.callback_subscribe, 10)
        
    def callback_subscribe(self, msg):
        self.get_logger().info('Received Message: %s' % msg.data)
        