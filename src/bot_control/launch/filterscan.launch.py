import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    rviz_config_dir = os.path.join(
        get_package_share_directory('bot_control'),
        'rviz',
        'bot_control_config.rviz')

    return LaunchDescription([
        Node(
            package='bot_control',
            executable='reading_laser.py',
            name='reading_laser',
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_dir],
            output='screen'
        )
    ])
