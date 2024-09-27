from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Launch the talker node with parameters for speed (v) and steering angle (d)
        Node(
            package='cpp_py_pkg', 
            executable='talker',          # Name of the talker node executable/script
            name='talker',
            parameters=[
                {'v': 1.0},  # Set the 'v' parameter to 1.0 (example value)
                {'d': 0.5}   # Set the 'd' parameter to 0.5 (example value)
            ]
        ),

        # Launch the relay node
        Node(
            package='cpp_py_pkg',  
            executable='relay',           # Name of the relay node executable/script
            name='relay'
        ),
    ])
