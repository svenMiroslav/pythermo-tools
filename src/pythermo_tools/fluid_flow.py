"""
Fluid flow related functions for pythermo_tools.

All inputs and outputs use SI units.
"""


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