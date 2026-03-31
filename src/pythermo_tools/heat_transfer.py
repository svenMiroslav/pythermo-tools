"""
Heat transfer related functions for pythermo_tools.

All inputs and outputs use SI units.
"""

def nusselt_vertical_plate_laminar(Ra):
    """
    Calculate Nusselt number for laminar natural convection
    on a vertical plate or vertical pipe.

    Parameters
    ----------
    Ra : float
        Rayleigh number [-]

    Returns
    -------
    Nu : float
        Nusselt number [-]

    Notes
    -----
    Valid for:

        Ra < 1e8

    Correlation:

        Nu = 0.52 * Ra**(1/4)
    """

    return 0.52 * Ra**0.25


def nusselt_vertical_plate_turbulent(Ra):
    """
    Calculate Nusselt number for turbulent natural convection
    on a vertical plate or vertical pipe.

    Parameters
    ----------
    Ra : float
        Rayleigh number [-]

    Returns
    -------
    Nu : float
        Nusselt number [-]

    Notes
    -----
    Valid for:

        Ra > 1e8

    Correlation for air:

        Nu = 0.10 * Ra**(1/3)
    """

    return 0.10 * Ra**(1.0 / 3.0)