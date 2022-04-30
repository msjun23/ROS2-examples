import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image, Imu

from cv_bridge import CvBridge

class ClientPublisher(Node):
    def __init__(self):
        super().__init__('my_controller_pub')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.__LinearVel = 0.0
        self.__AngularVel = 0.0
        
    def set_velocity(self, linear_vel, angular_vel):
        self.__LinearVel = linear_vel
        self.__AngularVel = angular_vel
    
    def timer_callback(self):
        msg = Twist()
        msg.linear.x = self.__LinearVel
        msg.angular.z = self.__AngularVel
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: %s' % msg)
        
class ClientSubscriber(Node):
    def __init__(self):
        super().__init__('my_controller_sub')
        self.subscriberImg = self.create_subscription(Image, '/camera/image_raw', self.listener_Img_callback, 10)
        # self.subscriberImu = self.create_subscription(Imu, '/imu', self.listener_Imu_callback, 10)
        
        self.Cv2Image = None
        self.CvBridge = CvBridge()
        
    def listener_Img_callback(self, msg):
        self.get_logger().info('Subscribed width: %s' % msg.width)
        self.get_logger().info('Subscribed height: %s' % msg.height)
        
        self.Cv2Image = self.CvBridge.imgmsg_to_cv2(msg, 'bgr8')
        
    def listener_Imu_callback(self, msg):
        self.get_logger().info('Subscribed imu: %s' % msg.linear_acceleration)
        
    def GetImage(self):
        return self.Cv2Image
    