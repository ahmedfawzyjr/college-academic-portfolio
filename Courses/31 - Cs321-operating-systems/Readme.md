# CS321: Operating Systems (نظم التشغيل)

**Course Code:** `CS321`  
**Academic Term:** Y3S2 (Year 3, Semester 6)  
**Credit Hours:** 3 Credit Hours  
**Curriculum Category:** Systems  
**Instruction Type:** Compulsory  
**Department:** Department of Computer Science, Future Academy  

---

## 📌 Overview
Operating Systems is an integral component of the computer science curriculum, providing in-depth theoretical foundations and practical application in OS Structures, System Calls & Interrupts, Processes, Threads & Multithreading Models, CPU Scheduling (FCFS, SJF, Priority, Round Robin). The course bridges fundamental concepts with engineering practice, culminating in a concrete software implementation: **Process Scheduling & Page Replacement Simulator**.

---

## 🔗 Prerequisites
- **Formal Prerequisites:** `CS222`, `CSC312`
- **Recommended Foundations:** See detailed [Prerequisites Document](./overview/prerequisites.md).

---

## 🎯 Learning Objectives
- Master the theoretical formulations and mathematical foundations of OS Structures, System Calls & Interrupts.
- Implement verifiable algorithms and architectures utilizing C++, C, POSIX Threads, Linux.
- Analyze computational trade-offs, complexity limits, and reliability factors.
- Complete and test the practical course engineering project: **Process Scheduling & Page Replacement Simulator**.

---

## 📚 Topics
1. **OS Structures, System Calls & Interrupts**
2. **Processes, Threads & Multithreading Models**
3. **CPU Scheduling (FCFS, SJF, Priority, Round Robin)**
4. **Process Synchronization, Mutex, Semaphores & Deadlocks**
5. **Memory Management: Paging, Segmentation & Virtual Memory**
6. **Page Replacement Algorithms (FIFO, LRU, Optimal)**

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
  - *Title:* Operating System Concepts
  - *Author:* Abraham Silberschatz, Peter B. Galvin, Greg Gagne
  - *Edition:* 10th Edition
  - *Publisher:* Wiley
  - *ISBN:* `978-1119800361`
  - *Publisher Link:* [Operating System Concepts](https://www.wiley.com)
- Complete reading list and topic-chapter mappings are indexed in [References](./references/books.md).

---

## 🧪 Labs
- [Lab 01](./labs/lab-01/README.md): Practical exercises in OS Structures, System Calls & Interrupts.
- [Lab 02](./labs/lab-02/README.md): Practical exercises in Processes, Threads & Multithreading Models.
- [Lab 03](./labs/lab-03/README.md): Applied laboratory experiments in CPU Scheduling (FCFS, SJF, Priority, Round Robin).

---

## 📝 Assignments
- Graded university assignments, problem sheets, starter code, and verified solutions are preserved in the [Assignments Directory](./assignments/).

---

## 🚀 Engineering Project
- **Project Title:** **[Process Scheduling & Page Replacement Simulator](./projects/README.md)**
- **Concepts Applied:** OS Structures, System Calls & Interrupts, Processes, Threads & Multithreading Models, CPU Scheduling (FCFS, SJF, Priority, Round Robin)
- **Implementation:** Python / Clean Architecture with automated unit tests.
- **Verification:** Run `python -m unittest discover projects/tests/`.

---

## 🛠️ Technologies
- **Primary Languages:** C++, C, POSIX Threads
- **Tooling & Environments:** C, POSIX Threads, Linux

---

## 🔄 Related Courses
- **Feeds From (Prerequisites):** `CS222`, `CSC312`
- **Leads Into (Downstream):** Directly supports upper-level computing courses and the **[iLearn Graduation Project Capstone](../../projects/capstone/ilearn-smart-education-platform/README.md)**.

---

## 📁 Repository Structure
```
31-cs321-operating-systems/
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
1. Formulate and solve domain problems within OS Structures, System Calls & Interrupts.
2. Build modular, well-tested code demonstrating clean architectural patterns.
3. Quantify performance, time/space bounds, and system limitations.

---

## ❓ Review Questions
1. *What fundamental challenge does Operating Systems address in computing?*
2. *What are the primary algorithmic or system trade-offs encountered in OS Structures, System Calls & Interrupts?*
3. *How do the concepts learned in this course apply to large-scale production architectures?*

---

## 💼 Interview Connection
- Core principles taught in `CS321` appear frequently in technical coding interviews and systems design evaluations, particularly around OS Structures, System Calls & Interrupts and Processes, Threads & Multithreading Models.
