# utils/classifier.py

def classify_subject(query: str) -> str:
    query = query.lower()

    # Keywords for Math: Arithmetic, Algebra, Calculus, Geometry
    math_keywords = [
        "calculate", "solve", "add", "subtract", "multiply", "divide", "product", "sum", "difference", "remainder", "modulo",
        "equation", "x", "y", "z", "variable", "integrate", "derivative", "differential", "area", "perimeter", "geometry", "factor",
        "simplify", "expand", "square root", "quadratic", "cube", "expression", "+", "-", "*", "/", "=", "^", "value of"
    ]

    # Keywords for Physics: Classical Mechanics, Laws, Motion, Units
    physics_keywords = [
        "newton", "force", "velocity", "acceleration", "displacement", "mass", "gravity", "gravitational", "energy", "kinetic",
        "potential", "momentum", "inertia", "law of motion", "thermodynamics", "wave", "sound", "light", "motion", "frequency",
        "work", "joule", "newton's", "unit", "speed", "power", "voltage", "resistance", "current", "ohm", "magnet", "electric",
        "magnetic", "temperature", "friction"
    ]

    # Keywords for Chemistry: Structure, Reactions, Periodic Table, Bonds
    chemistry_keywords = [
        "atom", "molecule", "element", "compound", "reaction", "chemical", "acid", "base", "ph", "valence", "bond",
        "ionic", "covalent", "electron", "proton", "neutron", "table", "periodic", "formula", "oxidation", "reduction",
        "molar", "mass", "nucleus", "metal", "nonmetal", "alkali", "halogen", "solute", "solvent", "solution", "precipitate"
    ]

    if any(keyword in query for keyword in math_keywords):
        return "math"
    elif any(keyword in query for keyword in physics_keywords):
        return "physics"
    elif any(keyword in query for keyword in chemistry_keywords):
        return "chemistry"
    else:
        return "unknown"
