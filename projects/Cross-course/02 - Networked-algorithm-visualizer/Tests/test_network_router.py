"""
Unit Tests for Campus Network Router
"""

import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from network_router import CampusNetworkRouter

class TestCampusRouter(unittest.TestCase):
    def test_routing(self):
        router = CampusNetworkRouter()
        router.add_link("Library", "CS_Hall", 5.0)
        router.add_link("Library", "Student_Union", 10.0)
        router.add_link("CS_Hall", "Engineering_Lab", 3.0)
        router.add_link("Student_Union", "Engineering_Lab", 1.0)

        result = router.find_optimal_route("Library", "Engineering_Lab")
        self.assertEqual(result["total_latency_ms"], 8.0)  # Library -> CS_Hall (5) -> Eng (3) = 8
        self.assertEqual(result["optimal_path"], ["Library", "CS_Hall", "Engineering_Lab"])

if __name__ == '__main__':
    unittest.main()
