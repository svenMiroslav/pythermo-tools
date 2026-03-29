"""
Unit tests for properties.py module.

These tests verify correctness of fluid thermophysical property functions
used throughout the library.
"""

import pytest

from pythermo_tools.properties import (
    enthalpy_water_pT
)


def test_enthalpy_water_pT_standard_conditions():
    """
    Test specific enthalpy of water at standard conditions.

    Conditions:
        p = 101325 Pa
        T = 293.15 K (20 °C)
    """

    p = 101325.0   # Pa
    T = 293.15     # K

    h = enthalpy_water_pT(p, T)

    expected_h = 84000.0  # J/kg, reference value from CoolProp

    assert h == pytest.approx(
        expected_h,
        abs=2000.0,
        rel=0.02
    )


def test_enthalpy_water_pT_elevated_temperature():
    """
    Test specific enthalpy of water at elevated temperature.

    Conditions:
        p = 101325 Pa
        T = 353.15 K (80 °C)
    """

    p = 101325.0   # Pa
    T = 353.15     # K

    h = enthalpy_water_pT(p, T)

    expected_h = 335000.0  # J/kg, approximate reference value from CoolProp

    assert h == pytest.approx(
        expected_h,
        abs=5000.0,
        rel=0.02
    )