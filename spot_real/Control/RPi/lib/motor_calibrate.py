#!/usr/bin/env python

import time
from servo_model import ServoJoint

joint_names = [
    'rb_servo_r_hip', 'r_hip_r_thigh', 'r_thigh_r_knee', 'r_knee_r_shin',
    'r_shin_r_ankle', 'r_ankle_r_foot', 'lb_servo_l_hip', 'l_hip_l_thigh',
    'l_thigh_l_knee', 'l_knee_l_shin', 'l_shin_l_ankle', 'l_ankle_l_foot',
    'torso_r_shoulder', 'r_shoulder_rs_servo', 're_servo_r_elbow',
    'torso_l_shoulder', 'l_shoulder_ls_servo', 'le_servo_l_elbow'
]
loop = True

calib = input("Calibration [c] or Test [t]?: ")
pwm_min = int(input("Enter Min PWM: "))
pwm_max = int(input("Enter Max PWM: "))

while loop:
    channel = int(
        input("Which channel is your servo connected to? [0-11]: "))
    servo = ServoJoint(name=joint_names[channel],
                       pwm_chan=channel,
                       pwm_min=pwm_min,
                       pwm_max=pwm_max)

    val = float(input("Select a HIGH angle value (rad): "))
    servo.actuate(val)
    val = float(input("Select a LOW angle value (rad): "))
    servo.actuate(val)

    cont = input("Test another motor [y] or quit [n]? ")

    if cont == "n":
        loop = False
