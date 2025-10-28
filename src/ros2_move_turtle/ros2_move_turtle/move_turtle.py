import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import random


class MoveTurtle(Node):
    def __init__(self):
        super().__init__('move_turtle')
        
        # Suscriptor al tópico /turtle1/pose
        self.subscription = self.create_subscription(Pose,'/turtle1/pose',self.pose_callback,10)
        self.subscription
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.addition_x=0.1
    def pose_callback(self, msg):
        twist = Twist()

        # Si la posición supera 7 en x o y → detener
        if msg.x > 7.0 or msg.y > 7.0:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            self.get_logger().info('¡Límite alcanzado! La tortuga se detiene.')
        else:
            twist.linear.x = self.addition_x   # avanza
            twist.angular.z = 0.5 # gira de forma 
            self.addition_x+=0.01
        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = MoveTurtle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
