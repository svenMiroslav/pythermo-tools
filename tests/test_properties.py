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
    thermal_conductivity_water_pT,
    prandtl_water_pT,
    density_air_pT,
    dynamic_viscosity_air_pT,
    kinematic_viscosity_air_pT,
    specific_heat_capacity_air_pT,
    thermal_conductivity_air_pT,
    prandtl_air_pT,
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
    Test specific enthalpy of water at elevated temperature and pressure.

    Conditions:
        p = 5 bar
        T = 353.15 K (80 °C)
    """

    p_bar = 5.0      # bar
    p = p_bar * 1e5  # Pa
    T = 353.15       # K

    h = enthalpy_water_pT(p, T)

    expected_h = 335310.0  # J/kg, reference value from FSB Heat Tables

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
    Test dynamic viscosity of water at elevated temperature and pressure.

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
    Test kinematic viscosity of water at elevated temperature and pressure.

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
    Test specific heat capacity of water at elevated temperature and pressure.

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


def test_thermal_conductivity_water_pT_standard_conditions():
    """
    Test thermal conductivity of water at standard conditions.

    Conditions:
        p = 1 bar
        T = 293.15 K (20 °C)
    """

    p_bar = 1.0
    p = p_bar * 1e5  # Pa
    T = 293.15       # K

    k = thermal_conductivity_water_pT(p, T)

    expected_k = 0.59846  # W/(m·K), reference value from FSB Heat Tables

    assert k == pytest.approx(
        expected_k,
        rel=0.02,
        abs=0.01
    )


def test_thermal_conductivity_water_pT_elevated_temperature():
    """
    Test thermal conductivity of water at elevated temperature and pressure.

    Conditions:
        p = 5 bar
        T = 353.15 K (80 °C)
    """

    p_bar = 5.0
    p = p_bar * 1e5  # Pa
    T = 353.15       # K

    k = thermal_conductivity_water_pT(p, T)

    expected_k = 0.67023  # W/(m·K), reference value from FSB Heat Tables

    assert k == pytest.approx(
        expected_k,
        rel=0.02,
        abs=0.01
    )


def test_prandtl_water_pT_standard_conditions():
    """
    Test Prandtl number of water at standard conditions.

    Conditions:
        p = 1 bar
        T = 293.15 K (20 °C)
    """

    p_bar = 1.0
    p = p_bar * 1e5  # Pa
    T = 293.15       # K

    Pr = prandtl_water_pT(p, T)

    expected_Pr = 7.0039  # reference value from FSB Heat Tables

    assert Pr == pytest.approx(
        expected_Pr,
        rel=0.04,
        abs=0.2
    )


def test_prandtl_water_pT_elevated_conditions():
    """
    Test Prandtl number of water at elevated temperature and pressure.

    Conditions:
        p = 5 bar
        T = 353.15 K (80 °C)
    """

    p_bar = 5.0
    p = p_bar * 1e5  # Pa
    T = 353.15       # K

    Pr = prandtl_water_pT(p, T)

    expected_Pr = 2.2184  # reference value from FSB Heat Tables

    assert Pr == pytest.approx(
        expected_Pr,
        rel=0.05,
        abs=0.15
    )


def test_density_air_pT_standard_conditions():
    """
    Test density of air at standard conditions.

    Conditions:
        p = 1 bar
        T = 293.15 K (20 °C)
    """

    p_bar = 1.0
    p = p_bar * 1e5  # Pa
    T = 293.15       # K

    rho = density_air_pT(p, T)

    expected_rho = 1.1884  # kg/m³, reference value from FSB Heat Tables

    assert rho == pytest.approx(
        expected_rho,
        rel=0.02,
        abs=0.02
    )


def test_density_air_pT_elevated_temperature():
    """
    Test density of air at elevated temperature.

    Conditions:
        p = 1 bar
        T = 353.15 K (80 °C)
    """

    p_bar = 1.0
    p = p_bar * 1e5  # Pa
    T = 353.15       # K

    rho = density_air_pT(p, T)

    expected_rho = 0.9865  # kg/m³, reference value from FSB Heat Tables

    assert rho == pytest.approx(
        expected_rho,
        rel=0.03,
        abs=0.03
    )


def test_dynamic_viscosity_air_pT_standard_conditions():
    """
    Test dynamic viscosity of air at standard conditions.

    Conditions:
        p = 1 bar
        T = 293.15 K (20 °C)
    """

    p_bar = 1.0
    p = p_bar * 1e5  # Pa
    T = 293.15       # K

    mu = dynamic_viscosity_air_pT(p, T)

    expected_mu = 18.206e-6  # Pa·s, reference value from FSB Heat Tables

    assert mu == pytest.approx(
        expected_mu,
        rel=0.03,
        abs=1e-6
    )


def test_dynamic_viscosity_air_pT_elevated_temperature():
    """
    Test dynamic viscosity of air at elevated temperature.

    Conditions:
        p = 1 bar
        T = 353.15 K (80 °C)
    """

    p_bar = 1.0
    p = p_bar * 1e5  # Pa
    T = 353.15       # K

    mu = dynamic_viscosity_air_pT(p, T)

    expected_mu = 20.947e-6  # Pa·s, reference value from FSB Heat Tables

    assert mu == pytest.approx(
        expected_mu,
        rel=0.03,
        abs=1e-6
    )


def test_kinematic_viscosity_air_pT_standard_conditions():
    """
    Test kinematic viscosity of air at standard conditions.

    Conditions:
        p = 1 bar
        T = 293.15 K (20 °C)
    """

    p_bar = 1.0
    p = p_bar * 1e5  # Pa
    T = 293.15       # K

    nu = kinematic_viscosity_air_pT(p, T)

    mu_tab = 18.206e-6   # Pa·s, reference value from FSB Heat Tables
    rho_tab = 1.1884   # kg/m³, reference value from FSB Heat Tables

    expected_nu = mu_tab / rho_tab

    assert nu == pytest.approx(
        expected_nu,
        rel=0.04,
        abs=1e-6
    )


def test_kinematic_viscosity_air_pT_elevated_temperature():
    """
    Test kinematic viscosity of air at elevated temperature.

    Conditions:
        p = 1 bar
        T = 353.15 K (80 °C)
    """

    p_bar = 1.0
    p = p_bar * 1e5  # Pa
    T = 353.15       # K

    nu = kinematic_viscosity_air_pT(p, T)

    mu_tab = 20.947e-6  # Pa·s, reference value from FSB Heat Tables
    rho_tab = 0.9865   # kg/m³, reference value from FSB Heat Tables

    expected_nu = mu_tab / rho_tab

    assert nu == pytest.approx(
        expected_nu,
        rel=0.04,
        abs=1e-6
    )


def test_specific_heat_capacity_air_pT_standard_conditions():
    """
    Test specific heat capacity of air at standard conditions.

    Conditions:
        p = 1 bar
        T = 293.15 K (20 °C)
    """

    p_bar = 1.0
    p = p_bar * 1e5  # Pa
    T = 293.15       # K

    cp = specific_heat_capacity_air_pT(p, T)

    expected_cp = 1006.0  # J/(kg·K), reference value from FSB Heat Tables

    assert cp == pytest.approx(
        expected_cp,
        rel=0.02,
        abs=20.0
    )


def test_specific_heat_capacity_air_pT_elevated_temperature():
    """
    Test specific heat capacity of air at elevated temperature.

    Conditions:
        p = 1 bar
        T = 353.15 K (80 °C)
    """

    p_bar = 1.0
    p = p_bar * 1e5  # Pa
    T = 353.15       # K

    cp = specific_heat_capacity_air_pT(p, T)

    expected_cp = 1010.8  # J/(kg·K), reference value from FSB Heat Tables

    assert cp == pytest.approx(
        expected_cp,
        rel=0.02,
        abs=20.0
    )


def test_thermal_conductivity_air_pT_standard_conditions():
    """
    Test thermal conductivity of air at standard conditions.

    Conditions:
        p = 1 bar
        T = 293.15 K (20 °C)
    """

    p_bar = 1.0
    p = p_bar * 1e5  # Pa
    T = 293.15       # K

    k = thermal_conductivity_air_pT(p, T)

    expected_k = 25.562e-3  # W/(m·K), reference value from FSB Heat Tables

    assert k == pytest.approx(
        expected_k,
        rel=0.03,
        abs=0.001
    )


def test_thermal_conductivity_air_pT_elevated_temperature():
    """
    Test thermal conductivity of air at elevated temperature.

    Conditions:
        p = 1 bar
        T = 353.15 K (80 °C)
    """

    p_bar = 1.0
    p = p_bar * 1e5  # Pa
    T = 353.15       # K

    k = thermal_conductivity_air_pT(p, T)

    expected_k = 29.859e-3  # W/(m·K), reference value from FSB Heat Tables

    assert k == pytest.approx(
        expected_k,
        rel=0.03,
        abs=0.001
    )


def test_prandtl_air_pT_standard_conditions():
    """
    Test Prandtl number of air at standard conditions.

    Conditions:
        p = 1 bar
        T = 293.15 K (20 °C)
    """

    p_bar = 1.0
    p = p_bar * 1e5  # Pa
    T = 293.15       # K

    Pr = prandtl_air_pT(p, T)

    mu_tab = 18.206e-6  # Pa·s, reference value from FSB Heat Tables
    cp_tab = 1006.0     # J/(kg·K), reference value from FSB Heat Tables
    k_tab = 25.562e-3   # W/(m·K), reference value from FSB Heat Tables

    expected_Pr = mu_tab * cp_tab / k_tab

    assert Pr == pytest.approx(
        expected_Pr,
        rel=0.05,
        abs=0.05
    )


def test_prandtl_air_pT_elevated_temperature():
    """
    Test Prandtl number of air at elevated temperature.

    Conditions:
        p = 1 bar
        T = 353.15 K (80 °C)
    """

    p_bar = 1.0
    p = p_bar * 1e5  # Pa
    T = 353.15       # K

    Pr = prandtl_air_pT(p, T)

    # Tabulated values
    mu_tab = 20.947e-6  # Pa·s, reference value from FSB Heat Tables
    cp_tab = 1010.8     # J/(kg·K), reference value from FSB Heat Tables
    k_tab = 29.859e-3   # W/(m·K), reference value from FSB Heat Tables

    expected_Pr = mu_tab * cp_tab / k_tab

    assert Pr == pytest.approx(
        expected_Pr,
        rel=0.05,
        abs=0.05
    )