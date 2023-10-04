
"""This module contains the function."""


import math


def ball(radius: float, acceleration: float, time: float, velocity: float = 0) -> int:
    """Find the angle of displacement of the point of initial contact with the surface.

    Args:
        radius: the radius of the ball,
        acceleration: acceleration of free fall, is a constant == 9.8,
        time: the time of the ball movement ,
        velocity: the velocity of the ball.

    Returns:
        int: degree
    """
    distance = velocity * time + 0.5 * acceleration * time**2
    angle = math.atan(distance / radius)
    balls = math.degrees(angle)

    if radius <= 0 or time <= 0:
        return 0
    
    return round(balls, 2)
