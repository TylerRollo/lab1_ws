from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Launch the talker node with parameters for speed (v) and steering angle (d)
        Node(
            package='cpp_py_pkg', 
            executable='talker.py',      
            name='talker',
            parameters=[
                {'v': 1.0},  
                {'d': 0.5}   
            ]
        ),

        # Launch the relay node
        Node(
            package='cpp_py_pkg',  
            executable='relay.py',           # Name of the relay node executable/script
            name='relay'
        ),
    ])
