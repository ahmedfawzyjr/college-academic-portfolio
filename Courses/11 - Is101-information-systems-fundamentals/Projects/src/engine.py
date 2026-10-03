"""
Enterprise Information Architecture Blueprint
Course: IS101 — Information Systems Fundamentals
Clean Architecture Implementation.
"""

from typing import Dict, Any, List

class IS101Engine:
    def __init__(self):
        self.course_code = "IS101"
        self.course_name = "Information Systems Fundamentals"
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
        return ["Role of Information Systems in Business", "Hardware & Software Infrastructure", "Data Management & Business Intelligence", "E-Commerce & Digital Enterprise", "Enterprise Systems (ERP, CRM, SCM)", "Information Systems Security & Ethics"]
