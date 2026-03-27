"""
Unit tests for unit conversion functions in pythermo_tools.units.

These tests verify correctness of basic unit conversions
used throughout the library.
"""

import pytest

from pythermo_tools.units import (
    celsius_to_kelvin,
    kelvin_to_celsius,
    bar_to_pa,
    pa_to_bar,
)


def test_celsius_to_kelvin():
    """
    Test conversion from Celsius to Kelvin.

    Reference values:
    0 °C = 273.15 K
    20 °C = 293.15 K
    """

    assert celsius_to_kelvin(0) == 273.15
    assert celsius_to_kelvin(20) == 293.15


def test_kelvin_to_celsius():
    """
    Test conversion from Kelvin to Celsius.

    Reference values:
    273.15 K = 0 °C
    293.15 K = 20 °C
    """

    assert kelvin_to_celsius(273.15) == 0
    assert kelvin_to_celsius(293.15) == 20


def test_bar_to_pa():
    """
    Test conversion from bar to Pascal.

    Reference:
    1 bar = 100000 Pa
    """

    assert bar_to_pa(1) == 100000
    assert bar_to_pa(2) == 200000


def test_pa_to_bar():
    """
    Test conversion from Pascal to bar.

    Reference:
    100000 Pa = 1 bar
    """

    assert pa_to_bar(100000) == 1
    assert pa_to_bar(200000) == 2