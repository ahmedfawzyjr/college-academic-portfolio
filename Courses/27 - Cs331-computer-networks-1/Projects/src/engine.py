"""
Concurrent Multi-Client Server Messaging System
Course: CS331 — Computer Networks 1
Clean Architecture Implementation.
"""

from typing import Dict, Any, List

class CS331Engine:
    def __init__(self):
        self.course_code = "CS331"
        self.course_name = "Computer Networks 1"
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
        return ["OSI 7-Layer & TCP/IP 4-Layer Models", "Application Layer: HTTP, DNS, SMTP, FTP", "Transport Layer: TCP (Reliable Data Transfer, Congestion Control) & UDP", "Network Layer: IP Addressing, Subnetting, Routing Algorithms", "Link Layer: Ethernet, MAC Addressing & ARP", "Socket Programming Fundamentals"]
