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
    

# TODO:
# - density_water_pT
# - viscosity_water_pT
# - cp_water_pT
# - density_air_pT
# - viscosity_air_pT
# - conductivity_air_pT
