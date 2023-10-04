"""Degree function."""
from math import pi


def degree(
    radius: float,
    acceleration: float,
    time: float,
    velocity: float = 0,
) -> float | str:
    """
    Find the place of a point on a ball.

    Args:
        radius: float - radius of the ball.
        acceleration: float - acceleration of the ball.
        time: float - how much time the ball rolls.
        velocity: float - i don't fucking know.

    Returns:
        float - place of the point on the ball.
        or
        str - error
    """
    if radius <= 0 or time <= 0:
        return 'Radius or time are less or equal than 0'
    full_circle = 360
    distance = velocity * time + (acceleration * time ** 2) / 2
    length = 2 * pi * radius
    return round((distance % length) / length * full_circle, 2)
