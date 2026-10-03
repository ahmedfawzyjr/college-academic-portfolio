"""
Unit Tests for iLearn Smart Educational Platform Core Backend
"""

import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from ilearn_service import ILearnPlatformService

class TestILearnPlatform(unittest.TestCase):
    def setUp(self):
        self.service = ILearnPlatformService()
        self.student = self.service.register_user("ahmed_fawzy", "ahmed@example.com", "STUDENT")
        self.instructor = self.service.register_user("dr_smith", "smith@example.com", "INSTRUCTOR")

        # Setup course spine
        self.cs101 = self.service.add_course("CS101", "Intro to CS", 3, self.instructor.user_id)
        self.cs111 = self.service.add_course("CS111", "C++ Programming", 3, self.instructor.user_id, prereqs=["CS101"])
        self.cs211 = self.service.add_course("CS211", "Data Structures", 3, self.instructor.user_id, prereqs=["CS111"])

    def test_user_registration(self):
        self.assertEqual(self.student.role, "STUDENT")
        self.assertEqual(self.instructor.role, "INSTRUCTOR")

    def test_prerequisite_enforcement(self):
        # Enrolling in CS111 before CS101 should fail
        with self.assertRaises(PermissionError):
            self.service.enroll_student(self.student.user_id, "CS111")

        # Enroll in CS101 first
        enroll_101 = self.service.enroll_student(self.student.user_id, "CS101")
        self.assertEqual(enroll_101.status, "ACTIVE")

        # Grade CS101 and finalize
        self.service.record_grade(self.student.user_id, "CS101", "Midterm", 28.0)
        self.service.record_grade(self.student.user_id, "CS101", "Final", 57.0)
        grade = self.service.finalize_course(self.student.user_id, "CS101")
        self.assertEqual(grade, "A-")

        # Now CS111 enrollment should succeed
        enroll_111 = self.service.enroll_student(self.student.user_id, "CS111")
        self.assertEqual(enroll_111.status, "ACTIVE")

    def test_student_analytics(self):
        self.service.enroll_student(self.student.user_id, "CS101")
        self.service.record_grade(self.student.user_id, "CS101", "Exam", 95.0)
        self.service.finalize_course(self.student.user_id, "CS101")

        analytics = self.service.compute_student_analytics(self.student.user_id)
        self.assertEqual(analytics["estimated_gpa"], 4.0)
        self.assertEqual(analytics["academic_standing"], "ACADEMIC_EXCELLENCE")

if __name__ == '__main__':
    unittest.main()
