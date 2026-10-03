# IS312: Database Systems 2 (قواعد البيانات 2)

**Course Code:** `IS312`  
**Academic Term:** Y3S2 (Year 3, Semester 6)  
**Credit Hours:** 3 Credit Hours  
**Curriculum Category:** Information Systems  
**Instruction Type:** Compulsory  
**Department:** Department of Computer Science, Future Academy  

---

## 📌 Overview
Database Systems 2 is an integral component of the computer science curriculum, providing in-depth theoretical foundations and practical application in Transaction Processing & ACID Properties, Concurrency Control (Locking, Timestamping, 2PL), Database Recovery Techniques (WAL, Checkpoints). The course bridges fundamental concepts with engineering practice, culminating in a concrete software implementation: **ACID Transaction & High-Concurrency Banking Database Engine**.

---

## 🔗 Prerequisites
- **Formal Prerequisites:** `IS211`
- **Recommended Foundations:** See detailed [Prerequisites Document](./overview/prerequisites.md).

---

## 🎯 Learning Objectives
- Master the theoretical formulations and mathematical foundations of Transaction Processing & ACID Properties.
- Implement verifiable algorithms and architectures utilizing PostgreSQL, PL/pgSQL, Redis, MongoDB.
- Analyze computational trade-offs, complexity limits, and reliability factors.
- Complete and test the practical course engineering project: **ACID Transaction & High-Concurrency Banking Database Engine**.

---

## 📚 Topics
1. **Transaction Processing & ACID Properties**
2. **Concurrency Control (Locking, Timestamping, 2PL)**
3. **Database Recovery Techniques (WAL, Checkpoints)**
4. **Query Processing & Optimization (Cost Estimation)**
5. **Stored Procedures, Triggers & PL/SQL**
6. **NoSQL Databases & Distributed Data Systems**

---

## 🏛️ Course Structure
The course is organized into synchronized academic modules:
- **Sessions & Lectures:** Weekly interactive lectures covering foundational theory ([Sessions Directory](./sessions/)).
- **Sections & Tutorials:** Applied problem sets and recitation notes ([Sections Directory](./sections/)).
- **Book Chapters:** Mapped readings from authoritative literature ([Chapters Directory](./chapters/)).
- **Laboratories:** Practical coding and experimental assignments ([Labs Directory](./labs/)).
- **Assignments:** Academic problem sets ([Assignments Directory](./assignments/)).
- **Course Engineering Project:** Production-grade implementation ([Projects Directory](./projects/)).

---

## 📖 Book & References
- **Primary Textbook:**
  - *Title:* Database System Concepts
  - *Author:* Abraham Silberschatz, Henry F. Korth, S. Sudarshan
  - *Edition:* 7th Edition
  - *Publisher:* McGraw-Hill
  - *ISBN:* `978-0078022159`
  - *Publisher Link:* [Database System Concepts](https://www.mheducation.com)
- Complete reading list and topic-chapter mappings are indexed in [References](./references/books.md).

---

## 🧪 Labs
- [Lab 01](./labs/lab-01/README.md): Practical exercises in Transaction Processing & ACID Properties.
- [Lab 02](./labs/lab-02/README.md): Practical exercises in Concurrency Control (Locking, Timestamping, 2PL).
- [Lab 03](./labs/lab-03/README.md): Applied laboratory experiments in Database Recovery Techniques (WAL, Checkpoints).

---

## 📝 Assignments
- Graded university assignments, problem sheets, starter code, and verified solutions are preserved in the [Assignments Directory](./assignments/).

---

## 🚀 Engineering Project
- **Project Title:** **[ACID Transaction & High-Concurrency Banking Database Engine](./projects/README.md)**
- **Concepts Applied:** Transaction Processing & ACID Properties, Concurrency Control (Locking, Timestamping, 2PL), Database Recovery Techniques (WAL, Checkpoints)
- **Implementation:** Python / Clean Architecture with automated unit tests.
- **Verification:** Run `python -m unittest discover projects/tests/`.

---

## 🛠️ Technologies
- **Primary Languages:** PostgreSQL, PL/pgSQL, Redis
- **Tooling & Environments:** PL/pgSQL, Redis, MongoDB

---

## 🔄 Related Courses
- **Feeds From (Prerequisites):** `IS211`
- **Leads Into (Downstream):** Directly supports upper-level computing courses and the **[iLearn Graduation Project Capstone](../../projects/capstone/ilearn-smart-education-platform/README.md)**.

---

## 📁 Repository Structure
```
35-is312-database-systems-2/
├── README.md                  # Master course syllabus and guide
├── overview/
│   ├── objectives.md          # Formal academic objectives
│   ├── prerequisites.md       # Prerequisite network and dependencies
│   └── learning-outcomes.md   # Measurable competencies
├── syllabus/
│   └── syllabus.md            # Weekly breakdown and grading policy
├── sessions/                  # Lecture-by-lecture notes
├── sections/                  # Applied tutorials and recitation notes
├── chapters/                  # Textbook chapter cross-references
├── notes/                     # Theoretical and technical notes
├── labs/                      # Hands-on laboratory guides
├── assignments/               # Graded homework, solutions, tests
├── projects/                  # Real engineering project implementation
│   ├── src/                   # Runnable source code
│   └── tests/                 # Automated unit tests
└── references/                # Books, papers, and online documentation
```

---

## 🎓 Learning Outcomes
1. Formulate and solve domain problems within Transaction Processing & ACID Properties.
2. Build modular, well-tested code demonstrating clean architectural patterns.
3. Quantify performance, time/space bounds, and system limitations.

---

## ❓ Review Questions
1. *What fundamental challenge does Database Systems 2 address in computing?*
2. *What are the primary algorithmic or system trade-offs encountered in Transaction Processing & ACID Properties?*
3. *How do the concepts learned in this course apply to large-scale production architectures?*

---

## 💼 Interview Connection
- Core principles taught in `IS312` appear frequently in technical coding interviews and systems design evaluations, particularly around Transaction Processing & ACID Properties and Concurrency Control (Locking, Timestamping, 2PL).
