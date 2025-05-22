# tools/constants_lookup.py

physics_constants = {
    "speed of light": "299,792,458 m/s",
    "gravitational constant": "6.674 × 10^-11 N·(m/kg)^2",
    "planck's constant": "6.626 × 10^-34 J·s",
    "elementary charge": "1.602 × 10^-19 C",
    "boltzmann constant": "1.381 × 10^-23 J/K",
    "avogadro's number": "6.022 × 10^23 mol^-1",
    "gas constant": "8.314 J/(mol·K)",
    "acceleration due to gravity": "9.8 m/s²"
}

def get_physics_constant(query: str) -> str:
    query = query.lower()
    for key, value in physics_constants.items():
        if key in query:
            return f"The {key} is {value}."
    return None
