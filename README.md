# pythermo-tools

A Python thermodynamics and heat transfer toolbox for engineering calculations.

---

## Overview

`pythermo-tools` is a personal engineering library for thermodynamics, fluid flow, and heat transfer calculations.

The project is being developed step by step, with a strong focus on:

- SI units only  
- clear and explicit function naming  
- modular structure  
- unit-tested functions  
- engineering-oriented workflow  

---

## Current functionality

### Unit conversions

- Celsius ↔ Kelvin  
- bar ↔ Pa  

---

### Thermophysical properties

#### Water

- enthalpy from pressure and temperature  
- density  
- dynamic viscosity  
- kinematic viscosity  
- specific heat capacity  
- thermal conductivity  
- Prandtl number  

#### Air

- density  
- dynamic viscosity  
- kinematic viscosity  
- specific heat capacity  
- thermal conductivity  
- Prandtl number  

---

### Fluid flow

- Reynolds number from kinematic viscosity  
- Reynolds number from density and dynamic viscosity  

---

## Project structure

    src/pythermo_tools/
        constants.py
        fluid_flow.py
        heat_transfer.py
        properties.py
        thermodynamics.py
        units.py

    tests/
        test_fluid_flow.py
        test_properties.py
        test_units.py

---

## Installation

Clone the repository:

    git clone https://github.com/svenMiroslav/pythermo-tools.git
    cd pythermo-tools

Create and activate a virtual environment.

### Linux

    python3 -m venv .venv
    source .venv/bin/activate

### Windows (PowerShell)

    py -m venv .venv
    .\.venv\Scripts\Activate.ps1

Install dependencies:

    pip install pytest CoolProp

---

## Running tests

### Linux

    PYTHONPATH=src pytest

### Windows (PowerShell)

    $env:PYTHONPATH = "src"
    pytest

---

## Examples

### Water density at 20 °C and 1 bar

    from pythermo_tools.properties import density_water_pT
    from pythermo_tools.units import bar_to_pa, celsius_to_kelvin

    p = bar_to_pa(1.0)
    T = celsius_to_kelvin(20.0)

    rho = density_water_pT(p, T)
    print(rho)

---

### Reynolds number from kinematic viscosity

    from pythermo_tools.fluid_flow import reynolds_number

    Re = reynolds_number(
        v=0.5,
        L=0.01,
        nu=1.0e-6
    )

    print(Re)

---

## Validation

Property tests are checked against reference heat tables from:

University of Zagreb  
Faculty of Mechanical Engineering (FSB)  
Heat Tables  

Authors:  
B. Halasz  
A. Galović  
I. Boras  

CoolProp is used internally for thermophysical property evaluation.

---

## Roadmap

Planned next steps:

- Grashof number  
- Rayleigh number  
- Nusselt number correlations  
- heat transfer coefficient functions  
- thermodynamics module functions  
- pressure drop calculations  
- pump and pipe flow utilities  

---

## Notes

All inputs and outputs use SI units.

This project is developed incrementally using unit tests and verified reference data.