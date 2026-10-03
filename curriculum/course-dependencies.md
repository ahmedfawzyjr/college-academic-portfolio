# 🔗 Course Dependencies & Prerequisite Network

This document defines the formal prerequisite constraints, corequisite relationships, and academic tracks governing the Computer Science curriculum.

---

## 🎯 Prerequisite Policy Principles

1. **Strict Foundational Gating**: Foundational courses (such as Calculus `MA101`, C++ Programming `CS111`, and Intro to Computer `CS101`) must be completed before advancing into tier-2 core topics.
2. **Horizontal & Vertical Cohesion**: Theoretical concepts introduced in basic mathematics (such as Discrete Structures `CS201` and Linear Algebra `MA202`) directly feed into downstream implementations (Algorithms `CS213`, Machine Learning `CSC465-ML`, Computer Graphics `CS341`).
3. **Capstone Integration Requirement**: The Graduation Project (`CS499`) requires successful completion of the core engineering spine: Software Engineering (`CSC465`), Database Systems (`IS312`), Web Programming (`CS313`), and Mobile Applications (`CS415`).

---

## 🗺️ Dependency Breakdown by Track

### 1. Programming & Core Software Track
```
CS101 (Intro to CS) ──► CS111 (C++ Lang 1) ──► CS211 (Data Structures) ──► CS213 (Algorithms)
CS112 (Java)        ──► CS212 (OOP C++)     ──► CS214 (Visual C#)
                                            ──► CS313 (Web Programming) ──► CS415 (Mobile Dev)
                                            ──► CS314 (Python)
```

### 2. Systems, Architecture & Infrastructure Track
```
PH101 (Physics) ──► EL101 (Electronics) ──► CS221 (Digital Logic) ──► CS222 (Computer Arch)
                                                                  ──► EE242 (Logic Design)
CS222 (Computer Arch) ──► CSC312 (System Programming) ──► CS321 (Operating Systems)
CS101 (Intro to CS)   ──► CS331 (Networks 1)         ──► CS451 (Information Security)
```

### 3. Mathematics, Theory & Statistics Track
```
MA101 (Calculus 1) ──► MA202 (Linear Algebra) ──► MA302 (Diff Equations)
                   ──► ST101 (Prob & Stats)   ──► MA301 (Operations Research)
                   ──► CS201 (Discrete Math)  ──► CS311 (Automata & Formal Languages)
```

### 4. Data, AI & Machine Learning Track
```
IS101 (IS Fundamentals) ──► IS211 (Database 1) ──► IS312 (Database 2)
                                               ──► CSC466 (Data Mining)
CS213 (Algorithms)      ──► CS441 (Artificial Intelligence) ──► CSC465-ML (Machine Learning)
MA202 + ST101                                              ──► CSC465-ML
CS341 (Computer Graphics) ──► CS444 (Image Processing 1)    ──► CS445 (Image Processing 2)
```

### 5. Software Engineering & Capstone Track
```
IS101 (IS) ──► IS211 (Database 1) ──► IS331 (System Analysis) ──► CSC465 (Software Eng) ──► CS499 (Graduation Project)
CS212 (OOP)                                                  ──► CSC465
HU104 (Management) ─────────────────► IS321 (Project Mgmt)
CS313 (Web) + IS312 (DB2) + CS415 (Mobile) ─────────────────────────────────────────────► CS499
```

---

## 📋 Comprehensive Course Dependency Table

| Course Code | Course Name | Semester | Strict Prerequisites | Recommended Corequisites |
|---|---|:---:|---|---|
| `CS101` | Introduction to Computer | Y1S1 | None | `CS112`, `MA101` |
| `CS112` | Java Programming | Y1S1 | None | `CS101` |
| `HU101` | Technical English 1 | Y1S1 | None | None |
| `HU104` | Principles of Management | Y1S1 | None | None |
| `MA101` | Mathematics 1 (Calculus) | Y1S1 | High School Math | None |
| `PH101` | General Physics (E&M) | Y1S1 | High School Physics | `MA101` |
| `CS111` | Programming Language 1 (C++) | Y1S2 | `CS101` | None |
| `EL101` | Computer Electronics | Y1S2 | `PH101` | None |
| `HU102` | Technical English 2 | Y1S2 | `HU101` | None |
| `HU103` | Principles of Economics | Y1S2 | None | None |
| `IS101` | Information Systems Fundamentals | Y1S2 | None | `CS101` |
| `ST101` | Probability & Statistics | Y1S2 | `MA101` | None |
| `CS201` | Discrete Structures | Y2S1 | `CS101`, `MA101` | None |
| `CS211` | Data Structures | Y2S1 | `CS111`, `CS112` | None |
| `CS212` | Programming Language 2 (OOP) | Y2S1 | `CS111`, `CS112` | `CS211` |
| `CS221` | Digital Logic Design | Y2S1 | `EL101` | None |
| `HU202` | Business Law & Ethics | Y2S1 | None | None |
| `MA202` | Mathematics 2 (Linear Algebra) | Y2S1 | `MA101` | None |
| `CS213` | Design & Analysis of Algorithms | Y2S2 | `CS211`, `CS201` | None |
| `CS214` | Visual Programming (C#) | Y2S2 | `CS212` | None |
| `CS222` | Computer Architecture & Organization | Y2S2 | `CS221` | None |
| `HU201` | Principles of Accounting | Y2S2 | None | `HU104` |
| `IS211` | Database Systems 1 | Y2S2 | `CS101`, `IS101` | None |
| `CS311` | Automata & Formal Languages | Y3S1 | `CS201` | None |
| `CS313` | Web Programming | Y3S1 | `CS111`, `IS211` | None |
| `CS314` | Python Programming | Y3S1 | `CS111`, `CS212` | None |
| `CS331` | Computer Networks 1 | Y3S1 | `CS101`, `CS222` | None |
| `CSC312` | System Programming | Y3S1 | `CS111`, `CS222` | None |
| `IS321` | Project Management | Y3S1 | `IS101`, `HU104` | None |
| `MA301` | Operations Research | Y3S1 | `MA202`, `ST101` | None |
| `CS321` | Operating Systems | Y3S2 | `CS222`, `CSC312` | None |
| `CS341` | Computer Graphics | Y3S2 | `CS111`, `MA202` | None |
| `HU301` | Technical Report Writing | Y3S2 | `HU102` | None |
| `HU302` | Principles of Marketing | Y3S2 | `HU104` | None |
| `IS312` | Database Systems 2 | Y3S2 | `IS211` | None |
| `IS331` | System Analysis & Design | Y3S2 | `IS101`, `IS211` | None |
| `MA302` | Mathematics 3 (Diff Equations) | Y3S2 | `MA101`, `MA202` | None |
| `TR301` | Microsoft Office Skills Training | Y3S2 | `CS101` | None |
| `CS441` | Artificial Intelligence | Y4S1 | `CS213`, `CS201` | None |
| `CS451` | Information Security | Y4S1 | `CS331`, `CS201` | None |
| `CS491` | Special Topics in Computer Science | Y4S1 | `CS313`, `CS314` | None |
| `CSC465` | Software Engineering | Y4S1 | `IS331`, `CS212` | None |
| `CSC466` | Data Mining | Y4S1 | `IS211`, `ST101` | None |
| `CS415` | Mobile Application Development | Y4S2 | `CS212`, `CS313` | None |
| `CS444` | Digital Image Processing 1 | Y4S2 | `CS341`, `MA202` | None |
| `CS445` | Digital Image Processing 2 | Y4S2 | `CS444` | None |
| `CSC465-ML` | Machine Learning | Y4S2 | `CS441`, `ST101`, `MA202` | None |
| `EE242` | Logic Design (Self Study) | Y4S2 | `CS221` | None |
| `HU401` | Creative Thinking & Innovation | Y4S2 | None | None |
| `CS499` | Graduation Project (Capstone) | Y4S1-S2 | `CSC465`, `CS313`, `IS312`, `CS415` | None |
