"""
Unit conversion functions for pythermo_tools.

All internal calculations in pythermo_tools use SI units.
These functions provide safe and explicit conversions.
"""


def celsius_to_kelvin(T_c):
    """
    Convert temperature from degrees Celsius to Kelvin.

    Parameters
    ----------
    T_c : float
        Temperature in degrees Celsius [°C]

    Returns
    -------
    T_k : float
        Temperature in Kelvin [K]
    """

    T_k = T_c + 273.15
    return T_k


def kelvin_to_celsius(T_k):
    """
    Convert temperature from Kelvin to degrees Celsius.

    Parameters
    ----------
    T_k : float
        Temperature in Kelvin [K]

    Returns
    -------
    T_c : float
        Temperature in degrees Celsius [°C]
    """

    T_c = T_k - 273.15
    return T_c


def bar_to_pa(p_bar):
    """
    Convert pressure from bar to Pascal.

    Parameters
    ----------
    p_bar : float
        Pressure in bar [bar]

    Returns
    -------
    p_pa : float
        Pressure in Pascal [Pa]
    """

    p_pa = p_bar * 1e5
    return p_pa


def pa_to_bar(p_pa):
    """
    Convert pressure from Pascal to bar.

    Parameters
    ----------
    p_pa : float
        Pressure in Pascal [Pa]

    Returns
    -------
    p_bar : float
        Pressure in bar [bar]
    """

    p_bar = p_pa / 1e5
    return p_bar
