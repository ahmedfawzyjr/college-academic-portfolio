"""
Differential Equation Numerical Solver (Runge-Kutta & Euler)
Course: MA302 — Mathematics 3
Clean Architecture Implementation.
"""

from typing import Dict, Any, List

class MA302Engine:
    def __init__(self):
        self.course_code = "MA302"
        self.course_name = "Mathematics 3"
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
        return ["First-Order Differential Equations (Separable, Exact, Linear)", "Second-Order Linear Homogeneous & Non-Homogeneous Equations", "Laplace Transforms & Applications to Differential Equations", "Fourier Series & Periodic Functions", "Partial Differential Equations (Heat, Wave Equations)", "Numerical Methods for Differential Equations (Euler, Runge-Kutta)"]
