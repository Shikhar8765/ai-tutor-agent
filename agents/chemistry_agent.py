# agents/chemistry_agent.py

from utils.llm import generate_response

class ChemistryAgent:
    def __init__(self):
        pass

    # Now accepts context
    def answer(self, query: str, context: str = "") -> str:
        return generate_response(f"You are a chemistry expert. Help with this chemistry question:\n{query}")
