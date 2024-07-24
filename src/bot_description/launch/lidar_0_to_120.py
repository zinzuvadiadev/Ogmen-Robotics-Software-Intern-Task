import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LaserScanReader(Node):
    def __init__(self):
        super().__init__('laser_scan_reader')
        self.filtered_scan_publisher = self.create_publisher(LaserScan, '/filtered_scan', 10)
        self.scan_subscription = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)

    def scan_callback(self, scan_msg):
        filtered_ranges = scan_msg.ranges[0:120]  
        filtered_scan = LaserScan()
        filtered_scan.header = scan_msg.header
        filtered_scan.angle_min = scan_msg.angle_min
        filtered_scan.angle_max = scan_msg.angle_min + 120.0 * scan_msg.angle_increment
        filtered_scan.angle_increment = scan_msg.angle_increment
        filtered_scan.range_min = scan_msg.range_min
        filtered_scan.range_max = scan_msg.range_max
        filtered_scan.ranges = filtered_ranges
        self.filtered_scan_publisher.publish(filtered_scan)

def main(args=None):
    rclpy.init(args=args)
    laser_scan_reader = LaserScanReader()
    rclpy.spin(laser_scan_reader)
    laser_scan_reader.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()