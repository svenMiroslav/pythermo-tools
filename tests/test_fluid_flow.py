"""
Unit tests for fluid_flow.py module.

These tests verify correctness of fundamental fluid flow functions.
"""

import pytest

from pythermo_tools.fluid_flow import (
    reynolds_number,
    reynolds_number_rho_mu,
)


def test_reynolds_number_basic_case():
    """
    Test Reynolds number for a simple reference case.

    Conditions:
        v = 1 m/s
        L = 0.01 m
        nu = 1e-6 m²/s

    Expected:
        Re = 10000
    """

    v = 1.0       # m/s
    L = 0.01      # m
    nu = 1e-6     # m²/s

    Re = reynolds_number(v, L, nu)

    expected_Re = 10000.0

    assert Re == pytest.approx(
        expected_Re,
        rel=1e-9,
        abs=1e-9
    )


def test_reynolds_number_water_pipe_case():
    """
    Test Reynolds number for water flow in a small pipe.

    Conditions:
        v = 0.5 m/s
        L = 0.01 m
        nu = 1.0e-6 m²/s

    Expected:
        Re = 5000
    """

    v = 0.5       # m/s
    L = 0.01      # m
    nu = 1.0e-6   # m²/s

    Re = reynolds_number(v, L, nu)

    expected_Re = 5000.0

    assert Re == pytest.approx(
        expected_Re,
        rel=1e-9,
        abs=1e-9
    )


def test_reynolds_number_rho_mu_basic_case():
    """
    Test Reynolds number using density and dynamic viscosity.

    Conditions:
        v = 1 m/s
        L = 0.01 m
        rho = 1000 kg/m³
        mu = 1e-3 Pa·s

    Expected:
        Re = 10000
    """

    v = 1.0         # m/s
    L = 0.01        # m
    rho = 1000.0    # kg/m³
    mu = 1e-3       # Pa·s

    Re = reynolds_number_rho_mu(v, L, rho, mu)

    expected_Re = 10000.0

    assert Re == pytest.approx(
        expected_Re,
        rel=1e-9,
        abs=1e-9
    )


def test_reynolds_number_consistency_nu_vs_rho_mu():
    """
    Test consistency between Reynolds number definitions:

        Re = v L / nu
        Re = rho v L / mu

    Using relation:

        nu = mu / rho
    """

    v = 0.5         # m/s
    L = 0.02        # m

    rho = 998.21    # kg/m³ (water at ~20°C)
    mu = 1.0016e-3  # Pa·s (water at ~20°C)

    nu = mu / rho

    Re_from_nu = reynolds_number(v, L, nu)

    Re_from_rho_mu = reynolds_number_rho_mu(
        v,
        L,
        rho,
        mu
    )

    assert Re_from_nu == pytest.approx(
        Re_from_rho_mu,
        rel=1e-9,
        abs=1e-9
    )