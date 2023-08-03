# AMECAR
## My Autonomous Media Capturing Robot Concept


<div style="display: flex; flex-direction: row; flex-wrap: wrap;">
  <figure style="margin-right: 20px; margin-bottom: 20px; flex: 1 1 300px;">
    <img src="/Images/CAD design.jpg" alt="" style="width: 100%; height: auto;">
    <figcaption>CAD designs</figcaption>
  </figure>
  <figure style="margin-right: 20px; margin-bottom: 20px; flex: 1 1 300px;">
    <img src="/Images/Initial.jpg" alt="" style="width: 100%; height: auto;">
    <figcaption>Initial development</figcaption>
  </figure>
  <figure style="flex: 1 1 300px;">
    <img src="/Images/AMeCar assembled.jpg" alt="" style="width: 100%; height: auto;">
    <figcaption>Fully Assembled</figcaption>
  </figure>
  <figure style="flex: 1 1 300px;">
    <img src="/Images/Public display.jpg" alt="" style="width: 100%; height: auto;">
    <figcaption>Public Display</figcaption>
  </figure>
    <figure style="flex: 1 1 300px;">
    <img src="/Images/Magazine Feature.jpg" alt="" style="width: 100%; height: auto;">
    <figcaption>Magazine Feature</figcaption>
  </figure>
</div>

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Components](#components)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#config)
- [Troubleshooting](#trouble)
- [Contributing](#contributing)
- [License](#license)
## [Introduction](#introduction)
AMECAR is an Autonomous Video Capturing Robot designed to keep a subject in frame while they move by intelligently tracking their face using a camera, analyzing the footage, and actuating its motors to follow the human subject. The robot can also accept feedback through hand signals to adjust its behavior. View a working Design [here](https://www.linkedin.com/posts/gerald-mbuthia-827450177_100daysoflearning-design-people-activity-6985985118850953216-q4ds?utm_source=share&utm_medium=member_desktop) 

This README provides detailed documentation for setting up, configuring, and using AMECAR for various applications.

## [Features](#features)
Face Tracking: AMECAR uses the camera and OpenCV to detect and track human faces in real-time, ensuring the subject remains in frame.

Autonomous Movement: The robot's motor control system, powered by the Arduino Mega and Motor Shield, enables autonomous movement and precise positioning.

Hand Signal Feedback: AMECAR is capable of interpreting hand signals, allowing users to provide instructions or adjust its behavior.

Python and C++ Integration: The project is built using Python for controlling the robot and processing video feed, and C++ for real-time motor control and performance.

## [Components](#components)
Arduino Mega: Acts as the brain of the robot and controls the motor movements.

Motor Shield: Enables smooth control of the 4 DC motors for precise motion.

Raspberry Pi 4: Processes the video feed and runs the face detection algorithm.

4x 18650 Batteries: Provides power to the robot for untethered operation.

Robot Frame and Chassis: The physical structure that holds all the components together.

## [Installation](#installation)
Clone the AMECAR repository to your local machine:
bash
Copy code
git clone https://github.com/your-username/amecar.git
cd amecar
Ensure you have Python (>= 3.6) and C++ compiler installed on your Raspberry Pi 4.

Install the required Python libraries:

Copy code
pip install opencv-python
pip install numpy
pip install imutils
Compile the C++ code for motor control:
Copy code
g++ -o motor_control motor_control.cpp -lwiringPi

## [Usage](#usage)
Connect the Arduino Mega, Motor Shield, and Raspberry Pi 4 to assemble the AMECAR robot.

Power on the robot using the 4x 18650 batteries or an alternative power source.

Run the Python script to start the robot:

Copy code
python amecar.py
The robot will start capturing video and searching for faces. Once a face is detected, the robot will track the subject's movement.

To provide hand signal feedback, simply raise your hand with a predefined gesture (e.g., a thumbs-up) to trigger a specific action or behavior.

## [Configuration](#config)
The AMECAR robot allows for some configuration options. These can be modified in the config.ini file:

motor_speed: Adjust the motor speed for smoother or faster movements.
face_detection_threshold: Set the confidence threshold for face detection (0.0 to 1.0).
hand_signal_mapping: Define the mapping of hand signals to specific robot actions.
Troubleshooting
If you encounter any issues or have questions, please check the Troubleshooting Guide for common problems and solutions.

## [Contributing](#contributing)
We welcome contributions from the community! If you'd like to contribute to AMECAR, please follow the guidelines outlined in CONTRIBUTING.md.

## [License](#license)
AMECAR is licensed under the MIT License, allowing you to modify and distribute the code for both personal and commercial use.
