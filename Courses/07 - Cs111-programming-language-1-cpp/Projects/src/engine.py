"""
Personal Expense Tracker & Financial CLI
Course: CS111 — Programming Language 1 (C++)
Clean Architecture Implementation.
"""

from typing import Dict, Any, List

class CS111Engine:
    def __init__(self):
        self.course_code = "CS111"
        self.course_name = "Programming Language 1 (C++)"
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
        return ["C++ Syntax & Compilers", "Control Structures & Loops", "Functions & Scope", "Pointers & Memory Addressing", "Arrays & C-Strings", "File I/O Streams & Structs"]
