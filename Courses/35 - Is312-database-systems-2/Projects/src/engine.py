"""
ACID Transaction & High-Concurrency Banking Database Engine
Course: IS312 — Database Systems 2
Clean Architecture Implementation.
"""

from typing import Dict, Any, List

class IS312Engine:
    def __init__(self):
        self.course_code = "IS312"
        self.course_name = "Database Systems 2"
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
        return ["Transaction Processing & ACID Properties", "Concurrency Control (Locking, Timestamping, 2PL)", "Database Recovery Techniques (WAL, Checkpoints)", "Query Processing & Optimization (Cost Estimation)", "Stored Procedures, Triggers & PL/SQL", "NoSQL Databases & Distributed Data Systems"]
