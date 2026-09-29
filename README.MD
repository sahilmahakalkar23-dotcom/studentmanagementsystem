# Student Result Management System

A lightweight, console-based Python application designed to manage student academic records, calculate scores, and evaluate grades.

\---

## Overview

The **Student Result Management System** provides an interactive command-line interface (CLI) to track and manage student performance across five subjects: Hindi, Maths, English, Physics, and Chemistry. The system automates grade determination, total score calculation, and percentage computation while allowing users to store, retrieve, update, and remove student profiles during runtime.

\---

## Features

* **Add Student Record**: Register a student with roll number, name, and marks across 5 subjects. Prevents duplicate roll number entries.
* **Automatic Calculations**: Computes total marks, percentage, and assigns grades based on percentage thresholds:

  * `S`: >= 90%
  * `A`: >= 80%$
  * `B`: >= 70%$
  * `C`: >= 60%$
  * `D`: >= 50%$
  * `F`: < 50%$
* **Display All Records**: Formats and lists all registered students along with their academic statistics.
* **Search Student**: Look up student records directly using their unique roll number.
* **Update Student**: Modify a student's name and marks, automatically recalculating totals, percentages, and grades.
* **Delete Student**: Remove a student entry from the database using their roll number.
* **Interactive Menu**: User-friendly numbered CLI menu with basic input validation.

\---

## Technologies \& Tools Used

* **Language**: Python 3.x
* **Core Modules \& Structures**: Built-in Python data structures (`dict`, `list`) with standard I/O
* **Dependencies**: None (pure standard library)

\---

## Steps to Install \& Run the Project

### Prerequisites

Ensure Python 3.x is installed on your system. You can check your version by running:

```bash
python --version
# or
python3 --version
```

### Installation

1. Clone or download the repository to your local machine:

```bash
   git clone https://github.com/sahilmahakalkar23-dotcom/studentmanagementsystem
   cd 
   ```

2. Ensure `project.py` is present in your working directory.

### Running the Application

Execute the Python script using your terminal or command prompt:

```bash
python project.py
# or
python3 project.py
```

\---

## Instructions for Testing

Follow the menu prompts to test each operational feature of the program:

### 1\. Test Adding a Student

1. Enter `1` at the main menu.
2. Provide a roll number (e.g., `101`) and a name (e.g., `Alice`).
3. Enter marks for Hindi, Maths, English, Physics, and Chemistry (e.g., `95`, `90`, `92`, `88`, `91`).
4. **Expected Result**: System confirms `"Student added successfully!"` and calculates Grade `S`.

### 2\. Test Duplicate Entry Validation

1. Enter `1` again.
2. Use the same roll number (`101`).
3. **Expected Result**: System prints `"Student already exists!"` and returns to the menu.

### 3\. Test Displaying Records

1. Enter `2` at the main menu.
2. **Expected Result**: System outputs all entered student details including roll number, marks list, total, percentage, and assigned grade.

### 4\. Test Search Functionality

1. Enter `3` at the main menu.
2. Provide roll number `101`.
3. **Expected Result**: Displays details for student `101` under the `"--- Student Found ---"` header.
4. Run `3` again with a non-existent roll number (e.g., `999`) to confirm `"Student not found."` is shown.

### 5\. Test Update Functionality

1. Enter `4` at the main menu.
2. Enter roll number `101`.
3. Provide an updated name and new marks (e.g., `75` across all subjects).
4. **Expected Result**: Prints `"Student updated successfully!"`. View the updated record using option `2` to confirm recalculated percentage (`75.00%`) and grade (`B`).

### 6\. Test Deletion

1. Enter `5` at the main menu.
2. Enter roll number `101`.
3. **Expected Result**: Displays `"Student deleted successfully!"`. Selecting option `2` afterward should report `"No student record found."`.

### 7\. Test Exit

1. Enter `6` at the main menu.
2. **Expected Result**: Displays `"Thank you for using the system!"` and exits the script cleanly.

