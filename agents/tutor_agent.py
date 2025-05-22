# agents/tutor_agent.py

from agents.math_agent     import MathAgent
from agents.physics_agent  import PhysicsAgent
from agents.chemistry_agent import ChemistryAgent
from utils.classifier      import classify_subject
from utils.memory          import MemoryBuffer

class TutorAgent:
    def __init__(self):
        self.math_agent      = MathAgent()
        self.physics_agent   = PhysicsAgent()
        self.chemistry_agent = ChemistryAgent()
        self.memory          = MemoryBuffer(max_history=10)

    def handle_query(self, query: str) -> str:
        # 1) record user
        self.memory.add_query(query)

        # 2) grab full conversation context
        context = self.memory.get_context()

        # 3) route by subject
        subject = classify_subject(query)

        if subject == "math":
            response = self.math_agent.answer(query, context)
        elif subject == "physics":
            response = self.physics_agent.answer(query, context)
        elif subject == "chemistry":
            response = self.chemistry_agent.answer(query, context)
        else:
            response = "Sorry, I don't understand this subject yet."

        # 4) record tutor response
        self.memory.add_response(response)
        return response
