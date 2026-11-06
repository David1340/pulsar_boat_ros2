
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    mavros_node = Node(
        package='mavros',
        executable='mavros_node',
        name='mavros',
        output='screen',
        parameters=[{
            'fcu_url': 'udp://@192.168.2.2:14551',
            'system_id': 255,
            'target_system_id': 1,
        }]
    )

    livox_launch_file = os.path.join(
        get_package_share_directory('livox_ros_driver2'),
        'launch_ROS2',
        'msg_MID360_launch.py'
    )

    livox_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(livox_launch_file)
    )

    return LaunchDescription([
        mavros_node,
        livox_launch,
    ])
