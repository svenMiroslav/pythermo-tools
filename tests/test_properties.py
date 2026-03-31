"""
Unit tests for properties.py module.

These tests verify correctness of fluid thermophysical property functions
used throughout the library.

Reference data:
---------------
University of Zagreb
Faculty of Mechanical Engineering (FSB)
Heat Tables

Authors:
B. Halasz, A. Galović, I. Boras

Tolerance notes:
----------------
Absolute and relative tolerances are selected to account for
differences between tabulated values and CoolProp property models.
"""

import pytest

from pythermo_tools.properties import (
    enthalpy_water_pT,
    density_water_pT,
    dynamic_viscosity_water_pT,
    kinematic_viscosity_water_pT,
    specific_heat_capacity_water_pT,
)


def test_enthalpy_water_pT_standard_conditions():
    """
    Test specific enthalpy of water at standard conditions.

    Conditions:
        p = 1 bar
        T = 293.15 K (20 °C)
    """

    p_bar = 1.0      # bar
    p = p_bar * 1e5  # Pa
    T = 293.15       # K

    h = enthalpy_water_pT(p, T)

    expected_h = 84010.0  # J/kg, reference value from FSB Heat Tables

    assert h == pytest.approx(
        expected_h,
        abs=800,
        rel=0.01
    )


def test_enthalpy_water_pT_elevated_temperature():
    """
    Test specific enthalpy of water at elevated temperature.

    Conditions:
        p = 1 bar
        T = 353.15 K (80 °C)
    """

    p_bar = 1.0      # bar
    p = p_bar * 1e5  # Pa
    T = 353.15       # K

    h = enthalpy_water_pT(p, T)

    expected_h = 334990.0  # J/kg, approximate reference value from FSB Heat Tables

    assert h == pytest.approx(
        expected_h,
        abs=5000.0,
        rel=0.02
    )


def test_density_water_pT_standard_conditions():
    """
    Test density of water at standard conditions.

    Conditions:
        p = 1 bar
        T = 293.15 K (20 °C)
    """

    p_bar = 1.0      # bar
    p = p_bar * 1e5  # Pa
    T = 293.15       # K

    rho = density_water_pT(p, T)

    expected_rho = 998.21  # kg/m³, reference value from FSB Heat Tables

    assert rho == pytest.approx(
        expected_rho,
        abs=1.5,
        rel=0.0015
    )


def test_density_water_pT_elevated_conditions():
    """
    Test density of water at elevated temperature and pressure.

    Conditions:
        p = 5 bar
        T = 353.15 K (80 °C)
    """

    p_bar = 5.0      # bar
    p = p_bar * 1e5  # Pa
    T = 353.15       # K

    rho = density_water_pT(p, T)

    expected_rho = 972.01  # kg/m³, reference value from FSB Heat Tables

    assert rho == pytest.approx(
        expected_rho,
        abs=1.5,
        rel=0.0015
    )


def test_dynamic_viscosity_water_pT_standard_conditions():
    """
    Test dynamic viscosity of water at standard conditions.

    Conditions:
        p = 1 bar
        T = 293.15 K (20 °C)
    """

    p_bar = 1.0
    p = p_bar * 1e5  # Pa
    T = 293.15       # K

    mu = dynamic_viscosity_water_pT(p, T)

    expected_mu = 1001.61e-6  # Pa·s, reference value from FSB Heat Tables

    assert mu == pytest.approx(
        expected_mu,
        rel=0.02,
        abs=2e-5
    )


def test_dynamic_viscosity_water_pT_elevated_temperature():
    """
    Test dynamic viscosity of water at elevated temperature.

    Conditions:
        p = 5 bar
        T = 353.15 K (80 °C)
    """

    p_bar = 5.0
    p = p_bar * 1e5  # Pa
    T = 353.15       # K

    mu = dynamic_viscosity_water_pT(p, T)

    expected_mu = 354.46e-6  # Pa·s, reference value from FSB Heat Tables

    assert mu == pytest.approx(
        expected_mu,
        rel=0.03,
        abs=1e-5
    )


def test_kinematic_viscosity_water_pT_standard_conditions():
    """
    Test kinematic viscosity of water at standard conditions.

    Conditions:
        p = 1 bar
        T = 293.15 K (20 °C)
    """

    p_bar = 1.0
    p = p_bar * 1e5  # Pa
    T = 293.15       # K

    nu = kinematic_viscosity_water_pT(p, T)

    mu_tab = 1001.61e-6  # Pa·s, reference value from FSB Heat Tables
    rho_tab = 998.21     # kg/m³, reference value from FSB Heat Tables

    expected_nu = mu_tab / rho_tab  # m²/s

    assert nu == pytest.approx(
        expected_nu,
        rel=0.03,
        abs=3e-8
    )


def test_kinematic_viscosity_water_pT_elevated_temperature():
    """
    Test kinematic viscosity of water at elevated temperature.

    Conditions:
        p = 5 bar
        T = 353.15 K (80 °C)
    """

    p_bar = 5.0
    p = p_bar * 1e5  # Pa
    T = 353.15       # K

    nu = kinematic_viscosity_water_pT(p, T)

    mu_tab = 354.46e-6   # Pa·s, reference value from FSB Heat Tables
    rho_tab = 972.01     # kg/m³, reference value from FSB Heat Tables

    expected_nu = mu_tab / rho_tab  # m²/s

    assert nu == pytest.approx(
        expected_nu,
        rel=0.04,
        abs=5e-8
    )


def test_specific_heat_capacity_water_pT_standard_conditions():
    """
    Test specific heat capacity of water at standard conditions.

    Conditions:
        p = 1 bar
        T = 293.15 K (20 °C)
    """

    p_bar = 1.0
    p = p_bar * 1e5  # Pa
    T = 293.15       # K

    cp = specific_heat_capacity_water_pT(p, T)

    expected_cp = 4184.8  # J/(kg·K), reference value from FSB Heat Tables

    assert cp == pytest.approx(
        expected_cp,
        rel=0.01,
        abs=50.0
    )


def test_specific_heat_capacity_water_pT_elevated_temperature():
    """
    Test specific heat capacity of water at elevated temperature.

    Conditions:
        p = 5 bar
        T = 353.15 K (80 °C)
    """

    p_bar = 5.0
    p = p_bar * 1e5  # Pa
    T = 353.15       # K

    cp = specific_heat_capacity_water_pT(p, T)

    expected_cp = 4194.6  # J/(kg·K), reference value from FSB Heat Tables

    assert cp == pytest.approx(
        expected_cp,
        rel=0.01,
        abs=50.0
    )