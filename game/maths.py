import math

"""
Drivetrain transmission ratios:

1 gear | 3.56
2 gear | 2.53
3 gear | 1.68
4 gear | 1.02

"""

"""
# Input RPM, get speed
def speed(engine_rpm, wheel_diameter, drive_train_ratio):
    # Theoretical RPM
    rpm = engine_rpm / drive_train_ratio

    # Max RPM Reached
    if rpm >= 6500:
        return int(round((6500*wheel_diameter*math.pi*40)/63360))
    # Regular RPM Calculation
    else:
        return int(round((rpm*wheel_diameter*math.pi*40)/63360))
"""

def speed(rpm, gear, ratio):
    rpm /= 100
    return round((0.05*rpm**2-0.02*rpm)/ratio + 10*(gear-1))