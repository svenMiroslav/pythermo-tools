"""
CoolProp wrapper functions for pythermo_tools.

All inputs and outputs use SI units.
"""

from CoolProp.CoolProp import PropsSI


def water_enthalpy_pT(p, T):
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
        Specific enthalpy [J/kg]
    """

    h = PropsSI("H", "P", p, "T", T, "Water")
    return h
