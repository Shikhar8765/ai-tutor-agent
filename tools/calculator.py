# tools/calculator.py

import re
from sympy import Eq, solve, Symbol
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application
)

# Enable implicit multiplication (e.g., 3x → 3*x)
TRANSFORMATIONS = standard_transformations + (implicit_multiplication_application,)

def solve_expression(expr: str) -> str:
    try:
        # 1) Normalize unicode operators and strip punctuation
        s = expr.replace('÷', '/').replace('×', '*').strip().rstrip(' ?!.')

        # 2) Remove spaces and normalize exponent
        s = s.replace(' ', '').replace('^', '**')

        # 3) Equation handling
        if '=' in s:
            lhs, rhs = s.split('=', 1)
            var_m = re.search(r'[a-zA-Z]', s)
            if not var_m:
                return "No variable found in equation."
            var = Symbol(var_m.group())
            eq = Eq(
                parse_expr(lhs, transformations=TRANSFORMATIONS),
                parse_expr(rhs, transformations=TRANSFORMATIONS)
            )
            sol = solve(eq, var)
            return f"{var} = {sol[0]}" if sol else "No solution found."

        # 4) Pure arithmetic
        result = parse_expr(s, transformations=TRANSFORMATIONS)
        return str(result.evalf())

    except Exception as e:
        return f"Failed to evaluate expression: {str(e)}"
