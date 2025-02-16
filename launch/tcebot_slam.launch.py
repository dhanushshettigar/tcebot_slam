import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pkg_tcebot_slam = get_package_share_directory('tcebot_slam')

    # RViz
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', os.path.join(pkg_tcebot_slam, 'rviz', 'tcebot_rviz.rviz')],
    )

    return LaunchDescription([
        rviz,
    ])