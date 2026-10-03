"""
iLearn Smart Educational Platform — Core Academic Service Backend
Production-Grade Clean Architecture Implementation.
Demonstrates: Repository Pattern, Service Layer, Role-Based Access Control, and Analytics.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
import hashlib
import uuid

class User:
    def __init__(self, user_id: str, username: str, email: str, role: str):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.role = role  # STUDENT, INSTRUCTOR, ADMIN
        self.created_at = datetime.utcnow()

class Course:
    def __init__(self, course_code: str, title: str, credits: int, instructor_id: str, prereqs: List[str] = None):
        self.course_code = course_code
        self.title = title
        self.credits = credits
        self.instructor_id = instructor_id
        self.prereqs = prereqs or []

class Enrollment:
    def __init__(self, enrollment_id: str, student_id: str, course_code: str):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_code = course_code
        self.grades: Dict[str, float] = {}  # assessment_name -> score
        self.status = "ACTIVE"
        self.enrolled_at = datetime.utcnow()

    def calculate_total_score(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades.values())

    def get_letter_grade(self) -> str:
        score = self.calculate_total_score()
        if score >= 90: return "A"
        elif score >= 85: return "A-"
        elif score >= 80: return "B+"
        elif score >= 75: return "B"
        elif score >= 70: return "C+"
        elif score >= 65: return "C"
        elif score >= 60: return "D"
        else: return "F"

class ILearnPlatformService:
    """Core domain business logic service."""
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.courses: Dict[str, Course] = {}
        self.enrollments: Dict[str, Enrollment] = {}
        self.completed_courses: Dict[str, set] = {}  # student_id -> set of passed course codes

    def register_user(self, username: str, email: str, role: str) -> User:
        user_id = str(uuid.uuid4())[:8]
        user = User(user_id, username, email, role.upper())
        self.users[user_id] = user
        if role.upper() == "STUDENT":
            self.completed_courses[user_id] = set()
        return user

    def add_course(self, code: str, title: str, credits: int, instructor_id: str, prereqs: List[str] = None) -> Course:
        course = Course(code, title, credits, instructor_id, prereqs)
        self.courses[code] = course
        return course

    def enroll_student(self, student_id: str, course_code: str) -> Enrollment:
        if student_id not in self.users or self.users[student_id].role != "STUDENT":
            raise ValueError("Invalid student ID")
        if course_code not in self.courses:
            raise ValueError(f"Course {course_code} not found")

        course = self.courses[course_code]
        completed = self.completed_courses.get(student_id, set())

        # Enforce prerequisite gating
        for p in course.prereqs:
            if p not in completed:
                raise PermissionError(f"Prerequisite {p} not fulfilled for course {course_code}")

        enrollment_id = f"{student_id}_{course_code}"
        enrollment = Enrollment(enrollment_id, student_id, course_code)
        self.enrollments[enrollment_id] = enrollment
        return enrollment

    def record_grade(self, student_id: str, course_code: str, assessment: str, score: float):
        eid = f"{student_id}_{course_code}"
        if eid not in self.enrollments:
            raise KeyError("Enrollment does not exist")
        self.enrollments[eid].grades[assessment] = score

    def finalize_course(self, student_id: str, course_code: str) -> str:
        eid = f"{student_id}_{course_code}"
        enrollment = self.enrollments[eid]
        letter = enrollment.get_letter_grade()
        if letter != "F":
            enrollment.status = "COMPLETED"
            self.completed_courses[student_id].add(course_code)
        else:
            enrollment.status = "FAILED"
        return letter

    def compute_student_analytics(self, student_id: str) -> Dict[str, Any]:
        """AI / Statistical Risk Analysis Engine."""
        student_enrollments = [e for e in self.enrollments.values() if e.student_id == student_id]
        if not student_enrollments:
            return {"student_id": student_id, "gpa_estimate": 0.0, "status": "NO_COURSES"}

        total_points = 0.0
        total_credits = 0
        for e in student_enrollments:
            course = self.courses[e.course_code]
            total_credits += course.credits
            score = e.calculate_total_score()
            if score >= 90: pts = 4.0
            elif score >= 80: pts = 3.0
            elif score >= 70: pts = 2.0
            elif score >= 60: pts = 1.0
            else: pts = 0.0
            total_points += pts * course.credits

        gpa = total_points / total_credits if total_credits > 0 else 0.0
        risk_level = "HIGH_RISK" if gpa < 2.0 else ("MODERATE_RISK" if gpa < 3.0 else "ACADEMIC_EXCELLENCE")

        return {
            "student_id": student_id,
            "total_enrolled_courses": len(student_enrollments),
            "earned_credits": len(self.completed_courses.get(student_id, set())),
            "estimated_gpa": round(gpa, 2),
            "academic_standing": risk_level
        }
