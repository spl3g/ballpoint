"""Pytest function."""
import pytest

from main import degree

CIRCLES = (
    (1, 2, 3, 4, 123.21),
    (1, 1, 1, 0, 28.65),
    (0, 0, 0, 0, 'Radius or time are less or equal than 0'),
)


@pytest.mark.parametrize(
    'radius, acceleration, time, velocity, expected',
    CIRCLES,
)
def test_degree(
    radius: float,
    acceleration: float,
    time: float,
    velocity: float,
    expected: float | str,
) -> None:
    """
    Tests for the degree function.

    Args:
        radius: float
        acceleration: float
        time: float
        velocity: float
        expected: float | str

    Asserts:
        True if the answer is correct
    """
    assert expected == degree(radius, acceleration, time, velocity)
