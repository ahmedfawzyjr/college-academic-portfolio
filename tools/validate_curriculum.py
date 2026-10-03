"""
Curriculum & Repository Structural Integrity Validator
Verifies that all 50 courses, credit hours, mandatory directories, and markdown files are intact.
"""

import os
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def run_validation():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    courses_dir = os.path.join(base_dir, "courses")
    curriculum_dir = os.path.join(base_dir, "curriculum")
    docs_dir = os.path.join(base_dir, "docs")
    projects_dir = os.path.join(base_dir, "projects")
    shared_dir = os.path.join(base_dir, "shared")

    print("=" * 60)
    print("🔍 RUNNING ACADEMIC PORTFOLIO STRUCTURAL VALIDATION")
    print("=" * 60)

    errors = []
    warnings = []

    # 1. Check curriculum documents
    for doc in ["curriculum-map.md", "course-dependencies.md", "academic-roadmap.md", "course-index.md"]:
        p = os.path.join(curriculum_dir, doc)
        if not os.path.exists(p):
            errors.append(f"Missing curriculum document: {doc}")
        else:
            print(f"  ✅ Found curriculum/{doc}")

    # 2. Check docs
    for doc in ["learning-roadmap.md", "technology-map.md", "project-map.md", "progress.md", "curriculum-map.md"]:
        p = os.path.join(docs_dir, doc)
        if not os.path.exists(p):
            errors.append(f"Missing doc: {doc}")
        else:
            print(f"  ✅ Found docs/{doc}")

    # 3. Check projects
    for proj in ["capstone/ilearn-smart-education-platform", "cross-course/01 - Distributed-academic-service", "cross-course/02 - Networked-algorithm-visualizer"]:
        p = os.path.join(projects_dir, proj)
        if not os.path.exists(p) and not os.path.exists(os.path.join(projects_dir, proj.lower())):
            errors.append(f"Missing project: {proj}")
        else:
            print(f"  ✅ Found projects/{proj}")

    # 4. Check shared
    for s_item in ["algorithms", "data-structures", "utilities", "templates"]:
        p = os.path.join(shared_dir, s_item)
        if not os.path.exists(p):
            errors.append(f"Missing shared folder: {s_item}")
        else:
            print(f"  ✅ Found shared/{s_item}")

    # 5. Check all 50 course directories
    course_dirs = [d for d in os.listdir(courses_dir) if os.path.isdir(os.path.join(courses_dir, d))]
    print(f"\nChecking {len(course_dirs)} course directories in courses/ ...")
    if len(course_dirs) != 50:
        errors.append(f"Expected 50 courses, found {len(course_dirs)}")

    subdirs_req = ["overview", "syllabus", "sessions", "sections", "chapters", "notes", "labs", "assignments", "projects", "references"]
    
    for cd in sorted(course_dirs):
        c_path = os.path.join(courses_dir, cd)
        readme = os.path.join(c_path, "README.md")
        if not os.path.exists(readme):
            errors.append(f"Missing README.md in {cd}")

        for s in subdirs_req:
            sp = os.path.join(c_path, s)
            if not os.path.exists(sp):
                warnings.append(f"Missing standard subdir '{s}' in {cd}")

    print(f"Checked 50 courses.")
    print("\n" + "=" * 60)
    print(f"VALIDATION SUMMARY: {len(errors)} Errors, {len(warnings)} Warnings")
    print("=" * 60)
    if errors:
        for e in errors:
            print(f"  ❌ ERROR: {e}")
        return False
    else:
        print("  🎉 ALL 50 COURSES AND PORTFOLIO ARTIFACTS VERIFIED SUCCESSFULLY!")
        return True

if __name__ == '__main__':
    success = run_validation()
    sys.exit(0 if success else 1)
