# Problem Statement & Project Scope

## 1. Problem Statement

In many small academic setups, tutoring centers, and classrooms, student performance data is still handled manually on paper or through unstandardized spreadsheets. This manual workflow introduces significant drawbacks:

* **Calculation Errors**: Hand-calculating totals, percentages, and corresponding grades across multiple subjects often leads to human error.
* **Inefficient Retrieval**: Finding a specific student's report card or record requires sifting through physical files or large unindexed sheets.
* **Lack of Validation**: Manual systems often allow duplicate IDs or inconsistent grading thresholds without automatic warnings.
* **Overhead**: Managing basic administrative tasks (updating marks, re-evaluating grades, deleting alumni records) consumes unnecessary time for educators.

There is a clear need for a lightweight, dependency-free tool that automates result compilation, standardizes grading metrics, and provides quick record management.

---

## 2. Scope of the Project

### In-Scope
* **In-Memory CRUD Operations**: Creation, retrieval, modification, and deletion of student records within the application runtime.
* **Fixed Curricular Support**: Tracking marks across five core academic subjects: Hindi, Maths, English, Physics, and Chemistry.
* **Automated Assessment**: Deterministic calculation of total score, average percentage, and standard grade mapping ($S, A, B, C, D, F$).
* **Primary Key Enforcement**: Roll-number-based indexing to ensure no duplicate student identifiers exist.
* **Lightweight Execution**: Operable in any standard Python 3 command-line environment without external package dependencies.

### Out-of-Scope (Future Enhancements)
* **Persistent Storage**: Integration with external databases (e.g., SQLite, PostgreSQL) or flat files (`.csv`, `.json`) to save data across sessions.
* **Dynamic Curriculum**: User-definable subjects, varying maximum marks per subject, or modular credit-based weighting systems.
* **Authentication & Roles**: Multi-tier login systems (e.g., Administrator vs. Teacher vs. Student view).
* **Graphical User Interface (GUI)**: Desktop (Tkinter/PyQt) or web-based UI representations.

---

## 3. Target Users

* **Primary School & High School Teachers**: Educators needing a straightforward, fast tool to record term marks and instantly generate student grades without spreadsheet complexity.
* **Private Tutors & Coaching Centers**: Small educational businesses tracking batches of students across standardized subjects.
* **Academic Lab Instructors**: Instructors and evaluators who need to grade standardized laboratory modules or sectional exams.
* **Computer Science Students & Beginners**: Learners studying Python data structures (dictionaries, lists, functions, loops) who need a reference console application.

---

## 4. High-Level Features

| Feature Area | Description |
| :--- | :--- |
| **Record Creation & Validation** | Registers students via unique roll numbers; rejects duplicate registrations to ensure data integrity. |
| **Academic Performance Engine** | Computes cumulative marks, calculates exact percentage values, and applies conditional logic to assign letter grades. |
| **Record Search & Query** | Enables constant-time lookup ($O(1)$) by student roll number to view individual scorecards. |
| **Record Modification** | Allows updating student names and marks with automatic real-time recalculation of summary metrics. |
| **Record Pruning** | Enables safe deletion of records by roll number when students depart or records become obsolete. |
| **Interactive Terminal Interface** | A numbered, loop-driven CLI menu designed for intuitive keyboard navigation and error resilience against invalid menu options. |