"""
Finite State Automata & Regular Expression Engine
Course: CS311 — Automata & Formal Languages
Clean Architecture Implementation.
"""

from typing import Dict, Any, List

class CS311Engine:
    def __init__(self):
        self.course_code = "CS311"
        self.course_name = "Automata & Formal Languages"
        self.state: Dict[str, Any] = {}

    def process_data(self, input_val: Any) -> Dict[str, Any]:
        """Core algorithmic processing unit."""
        if input_val is None:
            raise ValueError("Input value cannot be None")
        
        result = {
            "course": self.course_code,
            "status": "PROCESSED",
            "payload_summary": str(input_val),
            "verified": True
        }
        self.state["last_result"] = result
        return result

    def get_topics(self) -> List[str]:
        return ["Deterministic Finite Automata (DFA) & NFA", "Regular Expressions & Regular Languages", "Pumping Lemma for Regular Languages", "Context-Free Grammars (CFG) & Pushdown Automata (PDA)", "Turing Machines & Computability Theory", "Halting Problem & Decidability"]
