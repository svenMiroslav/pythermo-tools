"""
Unit tests for heat_transfer.py module.

These tests verify correctness of heat transfer correlation functions.
"""

import pytest

from pythermo_tools.heat_transfer import (
    nusselt_vertical_plate_laminar,
    nusselt_vertical_plate_turbulent,
)


def test_nusselt_vertical_plate_laminar_basic_case():
    """
    Test laminar natural convection Nusselt number
    for a vertical plate.

    Conditions:
        Ra = 1e8

    Expected:
        Nu = 0.52 * Ra^(1/4)
    """

    Ra = 1.0e8

    Nu = nusselt_vertical_plate_laminar(Ra)

    expected_Nu = 0.52 * Ra**0.25

    assert Nu == pytest.approx(
        expected_Nu,
        rel=1e-9,
        abs=1e-9
    )


def test_nusselt_vertical_plate_laminar_typical_case():
    """
    Test laminar Nusselt number for a typical laminar regime.

    Conditions:
        Ra = 1e7

    Expected:
        Nu = 0.52 * Ra^(1/4)
    """

    Ra = 1.0e7

    Nu = nusselt_vertical_plate_laminar(Ra)

    expected_Nu = 0.52 * Ra**0.25

    assert Nu == pytest.approx(
        expected_Nu,
        rel=1e-9,
        abs=1e-9
    )


def test_nusselt_vertical_plate_turbulent_basic_case():
    """
    Test turbulent natural convection Nusselt number
    for a vertical plate or vertical pipe.

    Conditions:
        Ra = 1e10

    Expected:
        Nu = 0.10 * Ra^(1/3)
    """

    Ra = 1.0e10

    Nu = nusselt_vertical_plate_turbulent(Ra)

    expected_Nu = 0.10 * Ra**(1.0 / 3.0)

    assert Nu == pytest.approx(
        expected_Nu,
        rel=1e-9,
        abs=1e-9
    )


def test_nusselt_vertical_plate_turbulent_typical_case():
    """
    Test turbulent natural convection Nusselt number
    for a vertical plate or vertical pipe.

    Conditions:
        Ra = 1e9

    Expected:
        Nu = 0.10 * Ra^(1/3)
    """

    Ra = 1.0e9

    Nu = nusselt_vertical_plate_turbulent(Ra)

    expected_Nu = 0.10 * Ra**(1.0 / 3.0)

    assert Nu == pytest.approx(
        expected_Nu,
        rel=1e-9,
        abs=1e-9
    )