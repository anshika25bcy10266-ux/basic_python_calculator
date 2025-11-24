1. Cover Page

Project Title: Basic Python Calculator
Student Name: Anshika Srivastava
Registration Number: 25BCY10266
Program: B.Tech Computer Science in cyber security
Course: VITyarthi Project
Year: 2025
Institution: VIT Bhopal University


---

2. Introduction

This project is a simple Python-based calculator designed using modular programming principles. It performs basic arithmetic operations such as addition, subtraction, multiplication, division, modulus, power, and square root.
The goal of the project is to understand Python fundamentals, functional decomposition, folder structure, documentation, and GitHub usage.


---

3. Problem Statement

Students often require a lightweight, offline calculator that is free from advertisements and distractions. Existing tools are either too complex or too feature-heavy.
This project solves the need for a simple and easy-to-understand calculator using Python with clear module separation.


---

4. Functional Requirements

The calculator must be able to:

Take user input for numbers

Perform addition

Perform subtraction

Perform multiplication

Perform division (with zero-handling)

Perform modulus

Perform power calculation

Perform square root

Display results

Exit gracefully



---

5. Non-Functional Requirements

Usability: Easy menu-driven interface

Maintainability: Modular folder structure

Performance: Fast and efficient execution

Reliability: Handles invalid inputs and errors

Portability: Runs on any system with Python installed



---

6. System Architecture

+-----------------------+
               |      main.py          |
               |  (User Interface)     |
               +----------+------------+
                          |
        ----------------------------------------------
        |           |          |           |         |
  +-----v-----+ +---v----+ +---v----+ +----v----+ +--v-----+
  | addition  | | subtract| |multiply| | division| | modulus|
  +-----------+ +---------+ +---------+ +----------+ +--------+
                          |
                 +--------v---------+
                 |   power.py       |
                 +------------------+
                          |
                 +--------v----------+
                 | square_root.py    |
                 +-------------------+

             +-----------------------------+
             | utils / input_handler.py    |
             +-----------------------------+

             +-----------------------------+
             | tests / test_operations.py  |
             +-----------------------------+


---

7. Design Diagrams

a) Use Case Diagram (Text form)

User → Select Operation → System Performs Calculation → Shows Result

b) Workflow Diagram

Start
 ↓
Show Menu
 ↓
User selects operation
 ↓
Input numbers
 ↓
Perform calculation
 ↓
Show result
 ↓
Return to menu
 ↓
Exit


---

8. Design Decisions & Rationale

Modular Approach:
Each arithmetic operation is placed in a separate file to improve readability and maintainability.

Error Handling:
Division and modulus operations include zero-handling.

Testing Added:
A tests folder ensures all functions work correctly.

Menu-Driven CLI:
Easy for beginners and works on all systems without GUI.



---

9. Implementation Details

Programming Language: Python 3

Folder Structure:

main.py → contains menu and control flow

operations/ → contains all arithmetic modules

utils/ → input validation

tests/ → unit tests using pytest


Key Logic:

Takes input

Validates input

Calls specific module

Prints result




---

10. Screenshots / Output

(Add your own screenshots here or write this)

Screenshot 1: Menu displayed
![WhatsApp Image 2025-11-24 at 10 56 45 PM (1)](https://github.com/user-attachments/assets/9cf7b6d8-a25b-4817-aa0e-705620574cc5)

Screenshot 2: Operation performed 
![WhatsApp Image 2025-11-24 at 11 17 55 PM](https://github.com/user-attachments/assets/c8766931-f0fc-443b-8d90-72bb410da971)

Screenshot 3: Error handling message
![WhatsApp Image 2025-11-24 at 11 22 39 PM](https://github.com/user-attachments/assets/22cb0082-c96c-48a7-98a3-f6419af750ab)



---

11. Testing Approach

Testing was performed using pytest, covering:

Basic correct outputs for all operations

Edge case: division by zero

Edge case: modulus by zero

Edge case: negative square root


All tests passed successfully.


---

12. Challenges Faced

Learning structured folder setup

Understanding modular programming

Writing reusable functions

Creating unit tests

Uploading code properly to GitHub



---

13. Learnings & Key Takeaways

Improved Python coding fundamentals

Understood modular and reusable code design

Gained experience with GitHub version control

Confidence in writing tested and organized code

Better project documentation skills



---

14. Future Enhancements

Add GUI using Tkinter

Add scientific calculator features

Add calculation history

Add error logs

Add unit conversion utilities



---

15. References

Python Official Documentation

GeeksForGeeks – Python Modules

W3Schools – Python Basics

StackOverflow Discussions

VITyarthi Project Guidelines
*Name:* Anshika Srivastava  
*Registration Number:* 25BCY10266  
*Project Title:* Basic Python Calculator



