import re
from tools.constants_lookup import get_physics_constant
from utils.llm import generate_response

class PhysicsAgent:
    def __init__(self):
        pass

    def answer(self, query: str, context: str = "") -> str:
        low = query.strip().lower()

        # 1) Memory-based "remind me" handling
        if "remind me" in low or "remind" in low:
            # Look backward through conversation history
            for line in reversed(context.splitlines()):
                # Each history line: "Tutor: <response>"
                if line.lower().startswith("tutor:") and "speed of light" in line.lower():
                    # Return the stored tutor response without the prefix
                    return line[len("Tutor: "):]
            return "I don't have a previous value for that constant in memory."

        # 2) Constant lookup tool
        constant_value = get_physics_constant(query)
        if constant_value:
            return constant_value

        # 3) Fallback to LLM for conceptual questions
        return generate_response(f"You are a physics expert. Help with this question:\n{query}")
