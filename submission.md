# Lab 1: Intro to ROS 2

## Written Questions

### Q1: During this assignment, you've probably ran these two following commands at some point: ```source /opt/ros/foxy/setup.bash``` and ```source install/local_setup.bash```. Functionally what is the difference between the two?

Answer: ```source /opt/ros/foxy/setup.bash``` was used for ROS2 global installation and ```source install/local_setup.bash``` was for my workspace to have these packages.

### Q2: What does the ```queue_size``` argument control when creating a subscriber or a publisher? How does different ```queue_size``` affect how messages are handled?

Answer: ```queue_size``` is used to store the messages from the subscriber or publisher. The larger ```queue_size``` used, uses more memory but less messages are lost.

### Q3: Do you have to call ```colcon build``` again after you've changed a launch file in your package? (Hint: consider two cases: calling ```ros2 launch``` in the directory where the launch file is, and calling it when the launch file is installed with the package.)

Answer: No, only calling ```ros2 launch``` from the installed packages.