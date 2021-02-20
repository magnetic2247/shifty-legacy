import math

"""
Drivetrain transmission ratios:

1 gear | 3.56
2 gear | 2.53
3 gear | 1.68
4 gear | 1.02
5 gear | 0.79

"""

# Input RPM, get speed
def speed(engine_rpm, diameter, d_t_ratio):
    # Theoretical RPM
    rpm = engine_rpm/d_t_ratio

    # Max RPM Reached
    if rpm >= 6500:
        return (6500*diameter*math.pi*60)/63360
    # Regular RPM Calculation
    else:
        return (rpm*diameter*math.pi*60)/63360
