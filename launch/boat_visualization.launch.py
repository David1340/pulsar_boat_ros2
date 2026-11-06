
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory
import os
from launch_ros.actions import Node


def generate_launch_description():

    package_path = get_package_share_directory('pulsar_boat')

    urdf_file = os.path.join(
        package_path,
        'urdf',
        'pulsar_boat.urdf'
    )

    with open(urdf_file, 'r') as file:
        robot_description = file.read()

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[{
            'robot_description': robot_description
        }],
        output='screen'
    )

    rviz_config = os.path.join(
        get_package_share_directory('pulsar_boat'),
        'rviz',
        'pulsar_boat.rviz'
    )

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config],
        output='screen'
    )

    static_tf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_tf_publisher',
        arguments=[
            '0', '0', '0',
            '0', '0', '0',
            'world',
            'base_link'
        ],
        output='screen'
    )

    return LaunchDescription([
        robot_state_publisher,
        rviz,
        static_tf    
])
