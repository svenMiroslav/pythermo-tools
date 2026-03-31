"""
Fluid flow related functions for pythermo_tools.

All inputs and outputs use SI units.
"""

from pythermo_tools.constants import G_STANDARD


def reynolds_number(v, L, nu):
    """
    Calculate Reynolds number.

    Parameters
    ----------
    v : float
        Flow velocity [m/s]

    L : float
        Characteristic length [m]

    nu : float
        Kinematic viscosity [m²/s]

    Returns
    -------
    Re : float
        Reynolds number [-]

    Notes
    -----
    Reynolds number is calculated as:

        Re = v * L / nu
    """

    return v * L / nu


def reynolds_number_rho_mu(v, L, rho, mu):
    """
    Calculate Reynolds number using density and dynamic viscosity.

    Parameters
    ----------
    v : float
        Flow velocity [m/s]

    L : float
        Characteristic length [m]

    rho : float
        Fluid density [kg/m³]

    mu : float
        Dynamic viscosity [Pa·s]

    Returns
    -------
    Re : float
        Reynolds number [-]

    Notes
    -----
    Reynolds number is calculated as:

        Re = rho * v * L / mu
    """

    return rho * v * L / mu


def grashof_number(rho_o, rho_s, L, nu_s):
    """
    Calculate Grashof number using density difference.

    Parameters
    ----------
    rho_o : float
        Fluid density in the ambient region [kg/m³]

    rho_s : float
        Fluid density at the surface [kg/m³]

    L : float
        Characteristic length [m]

    nu_s : float
        Kinematic viscosity at surface temperature [m²/s]

    Returns
    -------
    Gr : float
        Grashof number [-]

    Notes
    -----
    General definition:

        Gr = (rho_o - rho_s) * G_STANDARD * L**3
             --------------------------------
                 rho_s * nu_s**2
    """

    return (rho_o - rho_s) * G_STANDARD * L**3 / (rho_s * nu_s**2)


def grashof_number_ideal_gas(T_s, T_o, L, nu_s):
    """
    Calculate Grashof number for ideal gases.

    Parameters
    ----------
    T_s : float
        Surface temperature [K]

    T_o : float
        Ambient temperature [K]

    L : float
        Characteristic length [m]

    nu_s : float
        Kinematic viscosity at surface temperature [m²/s]

    Returns
    -------
    Gr : float
        Grashof number [-]

    Notes
    -----
    For ideal gases:

        Gr = (T_s - T_o) * G_STANDARD * L**3
             -----------------------
                 T_o * nu_s**2
    """

    return (T_s - T_o) * G_STANDARD * L**3 / (T_o * nu_s**2)


def rayleigh_number(Gr, Pr):
    """
    Calculate Rayleigh number.

    Parameters
    ----------
    Gr : float
        Grashof number [-]

    Pr : float
        Prandtl number [-]

    Returns
    -------
    Ra : float
        Rayleigh number [-]

    Notes
    -----
    Rayleigh number is calculated as:

        Ra = Gr * Pr
    """

    return Gr * Pr