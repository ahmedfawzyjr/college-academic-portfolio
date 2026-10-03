# CS222: Computer Architecture & Organization (تنظيم وعمارة الحاسب)

**Course Code:** `CS222`  
**Academic Term:** Y2S2 (Year 2, Semester 4)  
**Credit Hours:** 3 Credit Hours  
**Curriculum Category:** Systems  
**Instruction Type:** Compulsory  
**Department:** Department of Computer Science, Future Academy  

---

## 📌 Overview
Computer Architecture & Organization is an integral component of the computer science curriculum, providing in-depth theoretical foundations and practical application in Instruction Set Architecture (ISA) & MIPS Assembly, Processor Datapath & Control Units, Pipelining & Pipeline Hazards (Data, Control, Structural). The course bridges fundamental concepts with engineering practice, culminating in a concrete software implementation: **MIPS Instruction Set CPU Emulator & Cache Simulator**.

---

## 🔗 Prerequisites
- **Formal Prerequisites:** `CS221`
- **Recommended Foundations:** See detailed [Prerequisites Document](./overview/prerequisites.md).

---

## 🎯 Learning Objectives
- Master the theoretical formulations and mathematical foundations of Instruction Set Architecture (ISA) & MIPS Assembly.
- Implement verifiable algorithms and architectures utilizing MIPS Assembly, MARS Simulator, C++.
- Analyze computational trade-offs, complexity limits, and reliability factors.
- Complete and test the practical course engineering project: **MIPS Instruction Set CPU Emulator & Cache Simulator**.

---

## 📚 Topics
1. **Instruction Set Architecture (ISA) & MIPS Assembly**
2. **Processor Datapath & Control Units**
3. **Pipelining & Pipeline Hazards (Data, Control, Structural)**
4. **Memory Hierarchy & Cache Design (Direct-mapped, Set-associative)**
5. **Virtual Memory & Translation Lookaside Buffers (TLB)**
6. **Input/Output Systems, Buses & DMA**

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
  - *Title:* Computer Organization and Design: The Hardware/Software Interface
  - *Author:* David A. Patterson, John L. Hennessy
  - *Edition:* 5th Edition
  - *Publisher:* Morgan Kaufmann
  - *ISBN:* `978-0124077263`
  - *Publisher Link:* [Computer Organization and Design: The Hardware/Software Interface](https://www.elsevier.com)
- Complete reading list and topic-chapter mappings are indexed in [References](./references/books.md).

---

## 🧪 Labs
- [Lab 01](./labs/lab-01/README.md): Practical exercises in Instruction Set Architecture (ISA) & MIPS Assembly.
- [Lab 02](./labs/lab-02/README.md): Practical exercises in Processor Datapath & Control Units.
- [Lab 03](./labs/lab-03/README.md): Applied laboratory experiments in Pipelining & Pipeline Hazards (Data, Control, Structural).

---

## 📝 Assignments
- Graded university assignments, problem sheets, starter code, and verified solutions are preserved in the [Assignments Directory](./assignments/).

---

## 🚀 Engineering Project
- **Project Title:** **[MIPS Instruction Set CPU Emulator & Cache Simulator](./projects/README.md)**
- **Concepts Applied:** Instruction Set Architecture (ISA) & MIPS Assembly, Processor Datapath & Control Units, Pipelining & Pipeline Hazards (Data, Control, Structural)
- **Implementation:** Python / Clean Architecture with automated unit tests.
- **Verification:** Run `python -m unittest discover projects/tests/`.

---

## 🛠️ Technologies
- **Primary Languages:** MIPS Assembly, MARS Simulator, C++
- **Tooling & Environments:** MARS Simulator, C++

---

## 🔄 Related Courses
- **Feeds From (Prerequisites):** `CS221`
- **Leads Into (Downstream):** Directly supports upper-level computing courses and the **[iLearn Graduation Project Capstone](../../projects/capstone/ilearn-smart-education-platform/README.md)**.

---

## 📁 Repository Structure
```
21-cs222-computer-architecture-and-organization/
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
1. Formulate and solve domain problems within Instruction Set Architecture (ISA) & MIPS Assembly.
2. Build modular, well-tested code demonstrating clean architectural patterns.
3. Quantify performance, time/space bounds, and system limitations.

---

## ❓ Review Questions
1. *What fundamental challenge does Computer Architecture & Organization address in computing?*
2. *What are the primary algorithmic or system trade-offs encountered in Instruction Set Architecture (ISA) & MIPS Assembly?*
3. *How do the concepts learned in this course apply to large-scale production architectures?*

---

## 💼 Interview Connection
- Core principles taught in `CS222` appear frequently in technical coding interviews and systems design evaluations, particularly around Instruction Set Architecture (ISA) & MIPS Assembly and Processor Datapath & Control Units.
