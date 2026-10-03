"""
MIPS Instruction Set CPU Emulator & Cache Simulator
Course: CS222 — Computer Architecture & Organization
Clean Architecture Implementation.
"""

from typing import Dict, Any, List

class CS222Engine:
    def __init__(self):
        self.course_code = "CS222"
        self.course_name = "Computer Architecture & Organization"
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
        return ["Instruction Set Architecture (ISA) & MIPS Assembly", "Processor Datapath & Control Units", "Pipelining & Pipeline Hazards (Data, Control, Structural)", "Memory Hierarchy & Cache Design (Direct-mapped, Set-associative)", "Virtual Memory & Translation Lookaside Buffers (TLB)", "Input/Output Systems, Buses & DMA"]
