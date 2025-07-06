from std_msgs.msg import String
import rclpy
from rclpy.node import Node

topicName='communication_topic'

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        
        self.subscriberCreated = self.create_subscription(String,topicName,self.callbackFunctionSubscriber, 10)
        self.subscriberCreated 
    
    def callbackFunctionSubscriber(self, receivedMessage):
        self.get_logger().info('We received the message:  "%s"' % receivedMessage.data)

def main(args=None):
    rclpy.init(args=args)
    subscriberNode = SubscriberNode()
    rclpy.spin(subscriberNode)
    subscriberNode.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()