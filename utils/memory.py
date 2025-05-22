# utils/memory.py

class MemoryBuffer:
    def __init__(self, max_history=5):
        self.max_history = max_history
        self.history = []

    def add_query(self, query):
        self._add_to_history(f"User: {query}")

    def add_response(self, response):
        self._add_to_history(f"Tutor: {response}")

    def _add_to_history(self, text):
        if len(self.history) >= self.max_history:
            self.history.pop(0)
        self.history.append(text)

    def get_context(self):
        return "\n".join(self.history)

    def clear(self):
        self.history = []
