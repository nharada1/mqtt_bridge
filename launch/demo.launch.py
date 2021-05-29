import launch
from launch import LaunchDescription
from launch_ros.actions import Node

from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'config_file',
            default_value='file://' + get_package_share_directory('mqtt_bridge') + '/config/demo.yaml'),
        Node(
            package='mqtt_bridge',
            executable='mqtt_bridge_node.py',
            namespace='mqtt_bridge',
            parameters=[
                {"config_file": LaunchConfiguration('config_file')}
            ]
        )
    ])
