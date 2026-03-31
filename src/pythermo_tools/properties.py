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


def thermal_conductivity_water_pT(p, T):
    """
    Calculate thermal conductivity of water from pressure and temperature.

    Parameters
    ----------
    p : float
        Pressure [Pa]
    T : float
        Temperature [K]

    Returns
    -------
    k : float
        Thermal conductivity of water [W/(m·K)]

    Notes
    -----
    Internally uses CoolProp property database.
    """

    return PropsSI("L", "P", p, "T", T, "Water")


def prandtl_water_pT(p, T):
    """
    Calculate Prandtl number of water from pressure and temperature.

    Parameters
    ----------
    p : float
        Pressure [Pa]
    T : float
        Temperature [K]

    Returns
    -------
    Pr : float
        Prandtl number of water [-]

    Notes
    -----
    Calculated from dynamic viscosity, specific heat capacity,
    and thermal conductivity.
    """

    mu = dynamic_viscosity_water_pT(p, T)
    cp = specific_heat_capacity_water_pT(p, T)
    k = thermal_conductivity_water_pT(p, T)

    return mu * cp / k


def density_air_pT(p, T):
    """
    Calculate density of air from pressure and temperature.

    Parameters
    ----------
    p : float
        Pressure [Pa]
    T : float
        Temperature [K]

    Returns
    -------
    rho : float
        Density of air [kg/m³]

    Notes
    -----
    Internally uses CoolProp property database.
    """

    return PropsSI("Dmass", "P", p, "T", T, "Air")


def dynamic_viscosity_air_pT(p, T):
    """
    Calculate dynamic viscosity of air from pressure and temperature.

    Parameters
    ----------
    p : float
        Pressure [Pa]
    T : float
        Temperature [K]

    Returns
    -------
    mu : float
        Dynamic viscosity of air [Pa·s]

    Notes
    -----
    Internally uses CoolProp property database.
    """

    return PropsSI("V", "P", p, "T", T, "Air")


def kinematic_viscosity_air_pT(p, T):
    """
    Calculate kinematic viscosity of air from pressure and temperature.

    Parameters
    ----------
    p : float
        Pressure [Pa]
    T : float
        Temperature [K]

    Returns
    -------
    nu : float
        Kinematic viscosity of air [m²/s]

    Notes
    -----
    Calculated as dynamic viscosity divided by density.
    """

    mu = dynamic_viscosity_air_pT(p, T)
    rho = density_air_pT(p, T)

    return mu / rho


def specific_heat_capacity_air_pT(p, T):
    """
    Calculate specific heat capacity of air from pressure and temperature.

    Parameters
    ----------
    p : float
        Pressure [Pa]
    T : float
        Temperature [K]

    Returns
    -------
    cp : float
        Specific heat capacity of air [J/(kg·K)]

    Notes
    -----
    Internally uses CoolProp property database.
    """

    return PropsSI("C", "P", p, "T", T, "Air")


def thermal_conductivity_air_pT(p, T):
    """
    Calculate thermal conductivity of air from pressure and temperature.

    Parameters
    ----------
    p : float
        Pressure [Pa]
    T : float
        Temperature [K]

    Returns
    -------
    k : float
        Thermal conductivity of air [W/(m·K)]

    Notes
    -----
    Internally uses CoolProp property database.
    """

    return PropsSI("L", "P", p, "T", T, "Air")


def prandtl_air_pT(p, T):
    """
    Calculate Prandtl number of air from pressure and temperature.

    Parameters
    ----------
    p : float
        Pressure [Pa]
    T : float
        Temperature [K]

    Returns
    -------
    Pr : float
        Prandtl number of air [-]

    Notes
    -----
    Calculated from dynamic viscosity, specific heat capacity,
    and thermal conductivity.
    """

    mu = dynamic_viscosity_air_pT(p, T)
    cp = specific_heat_capacity_air_pT(p, T)
    k = thermal_conductivity_air_pT(p, T)

    return mu * cp / k