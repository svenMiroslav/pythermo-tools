"""
Thermophysical property functions for pythermo_tools.

This module provides functions for calculating thermophysical
properties of fluids (e.g. water, air) using external property
libraries.

All inputs and outputs use SI units.

Naming convention:
------------------
property_fluid_inputPair

Examples:
    enthalpy_water_pT
    density_air_pT
"""

from CoolProp.CoolProp import PropsSI


def enthalpy_water_pT(p, T):
    """
    Calculate specific enthalpy of water from pressure and temperature.

    Parameters
    ----------
    p : float
        Pressure [Pa]
    T : float
        Temperature [K]

    Returns
    -------
    h : float
        Specific enthalpy of water [J/kg]

    Notes
    -----
    Internally uses CoolProp property database.
    """

    return PropsSI("H", "P", p, "T", T, "Water")


def density_water_pT(p, T):
    """
    Calculate density of water from pressure and temperature.

    Parameters
    ----------
    p : float
        Pressure [Pa]
    T : float
        Temperature [K]

    Returns
    -------
    rho : float
        Density of water [kg/m³]

    Notes
    -----
    Internally uses CoolProp property database.
    """

    return PropsSI("Dmass", "P", p, "T", T, "Water")


def dynamic_viscosity_water_pT(p, T):
    """
    Calculate dynamic viscosity of water from pressure and temperature.

    Parameters
    ----------
    p : float
        Pressure [Pa]
    T : float
        Temperature [K]

    Returns
    -------
    mu : float
        Dynamic viscosity of water [Pa·s]

    Notes
    -----
    Internally uses CoolProp property database.
    """

    return PropsSI("V", "P", p, "T", T, "Water")


def kinematic_viscosity_water_pT(p, T):
    """
    Calculate kinematic viscosity of water from pressure and temperature.

    Parameters
    ----------
    p : float
        Pressure [Pa]
    T : float
        Temperature [K]

    Returns
    -------
    nu : float
        Kinematic viscosity of water [m²/s]

    Notes
    -----
    Calculated as dynamic viscosity divided by density.
    """

    mu = dynamic_viscosity_water_pT(p, T)
    rho = density_water_pT(p, T)

    return mu / rho


def specific_heat_capacity_water_pT(p, T):
    """
    Calculate specific heat capacity of water from pressure and temperature.

    Parameters
    ----------
    p : float
        Pressure [Pa]
    T : float
        Temperature [K]

    Returns
    -------
    cp : float
        Specific heat capacity of water [J/(kg·K)]

    Notes
    -----
    Internally uses CoolProp property database.
    """

    return PropsSI("C", "P", p, "T", T, "Water")

# TODO:
# - cp_water_pT
# - density_air_pT
# - viscosity_air_pT
# - conductivity_air_pT
