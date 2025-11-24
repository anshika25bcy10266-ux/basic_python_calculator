## 1. Introduction
The Basic Python Calculator is a simple, modular command-line application developed as part of the VITyarthi project submission. It is designed to perform essential arithmetic operations while demonstrating good coding practices, documentation, and testing.

## 2. Problem Statement
Students often need a quick, distraction-free calculator that can run offline and perform basic mathematical operations. This project fulfills that need by providing a simple, modular Python-based calculator.

## 3. Objectives
- Build a modular Python calculator.
- Implement clean code using separate modules for each operation.
- Provide good documentation for project understanding.
- Add testing using pytest.
- Submit a well-structured GitHub repository.

## 4. Functional Requirements
- Addition
- Subtraction
- Multiplication
- Division (with zero handling)
- Modulus
- Power (a^b)
- Square Root (with negative number handling)

## 5. Non-Functional Requirements
- *Usability:* Simple CLI interface
- *Maintainability:* Modular code structure
- *Reliability:* Handles invalid inputs
- *Performance:* Fast execution

## 6. System Architecture

User → Menu → Select Operation → Input Numbers → Calculate → Output

## 7. Workflow Diagram (Text Version)

Start ↓ Show Menu ↓ User selects option ↓ If Square Root → ask 1 number Else → ask 2 numbers ↓ Perform operation ↓ Show result ↓ Return to menu ↓ Exit

## 8. Implementation Details
- The project uses multiple Python files:
  - main.py → central controller
  - operations/ → separate file for each arithmetic function
  - utils/input_handler.py → handles user input validation
  - tests/ → contains pytest test cases

## 9. Testing Approach
- Every arithmetic operation is tested using pytest
- Edge cases like:
  - Division by zero
  - Modulus by zero
  - Negative square root
  are handled and tested.

## 10. Screenshots / Results
(You can add screenshots of running the calculator here.)

## 11. Challenges Faced
- Designing modular structure
- Ensuring accurate input validation
- Writing neat documentation

## 12. Learnings & Key Takeaways
- File structuring for projects
- Modular programming
- Using GitHub effectively
- Writing clean documentation

## 13. Future Enhancements
- Add a GUI (Tkinter)
- Add more scientific functions
- Add history/caching feature

## 14. References
- Python Official Documentation  
- TutorialsPoint
