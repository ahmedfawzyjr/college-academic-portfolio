"""
Analog Circuit & Logic Gate Analysis Simulator
Course: EL101 — Computer Electronics
Clean Architecture Implementation.
"""

from typing import Dict, Any, List

class EL101Engine:
    def __init__(self):
        self.course_code = "EL101"
        self.course_name = "Computer Electronics"
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
        return ["Semiconductor Physics & PN Junction Diodes", "Diode Applications (Rectifiers, Clippers, Clampers)", "Bipolar Junction Transistors (BJT)", "Field-Effect Transistors (FET & MOSFET)", "Operational Amplifiers (Op-Amps)", "Digital Logic Gate Electronics"]
