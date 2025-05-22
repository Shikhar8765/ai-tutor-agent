# agents/math_agent.py

import re
from tools.calculator import solve_expression
from utils.llm       import generate_response

class MathAgent:
    def __init__(self):
        pass

    # <- now takes context
    def answer(self, query: str, context: str = "") -> str:
        text = query.strip().lower()

        # --- memory‐based follow‐up ---
        if any(verb in text for verb in ("multiply", "divide", "add", "subtract")):
            # extract the number to operate with
            m = re.search(
                r'(?:multiply|divide|add|subtract)\s+(?:that\s+result\s+)?(?:by\s+)?(\d+\.?\d*)',
                text
            )
            if m:
                factor = float(m.group(1))
                # pull last numeric answer from context
                nums = re.findall(r"The answer is: ([\d\.]+)", context)
                if nums:
                    last = float(nums[-1])
                    if "multiply" in text:
                        out = last * factor
                    elif "divide" in text:
                        out = last / factor if factor else "∞"
                    elif "add" in text:
                        out = last + factor
                    elif "subtract" in text:
                        out = last - factor
                    return f"The answer is: {out}"
            return "I need a number to operate with—please say, for example, 'multiply by 2'."

        # --- equation solving ---
        eq = re.search(r'(\d+(?:\.\d+)?\s*[\+\-\*\/\^]\s*\d+(?:\.\d+)?\s*=\s*\d+(?:\.\d+)?)', query)
        if eq:
            return f"The answer is: {solve_expression(eq.group(1))}"

        # --- pure arithmetic ---
        ar = re.search(r'(\d+(?:\.\d+)?(?:\s*[\+\-\*\/]\s*\d+(?:\.\d+)?)+)', query)
        if ar:
            return f"The answer is: {solve_expression(ar.group(1))}"

        # --- fallback to LLM ---
        return generate_response(f"You are a math expert. Help with this math question:\n{query}")
