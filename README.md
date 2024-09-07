
# Tkinter Scientific Calculator

## Overview

This is a scientific calculator built using Python's `Tkinter` library. The application allows users to perform a wide range of arithmetic, trigonometric, and logarithmic operations, along with factorials, combinations, and permutations.

## Features

- **Basic Arithmetic Operations**: Addition, Subtraction, Multiplication, Division.
- **Factorial Calculation**.
- **Trigonometric Functions**: Sine, Cosine, Tangent, and their inverses.
- **Logarithmic Functions**: Natural log (ln) and logarithm to base 10.
- **Power Functions**: Exponentials (`e^x`, `2^x`, `x^y`).
- **Combinations (nCr) and Permutations (nPr)**.
- **Reciprocal Calculation (`1/x`)**.
  
## Libraries Used

- `Tkinter`: For building the GUI interface.
- `numpy`: For handling advanced mathematical functions like trigonometry and logarithms.
- `tkinter.messagebox`: To show error messages for input validation.

## How to Run

### Prerequisites
Ensure that you have Python installed on your system. You can check this by running:
```bash
python --version
```

Install the required libraries:
```bash
pip install numpy
```

### Running the Calculator

1. Clone this repository or download the code files.
2. Open a terminal and navigate to the folder containing the script.
3. Run the Python file:
   ```bash
   python calculator.py
   ```

This will open up the GUI calculator.

## How to Use

1. **Input Fields**: There are two fields where users can input numbers.
   - Field 1: First number
   - Field 2: Second number (if required for the operation).
2. **Operations**: You can select any of the operations available on the calculator. The result will be displayed in the "Answer is" section.
3. **Error Handling**: For invalid inputs or operations like division by zero, the application shows a message box to prompt users to retry.

### Supported Operations:
- **Addition**: Adds the numbers from both fields.
- **Subtraction**: Subtracts the second number from the first.
- **Multiplication**: Multiplies the two numbers.
- **Division**: Divides the first number by the second.
- **Factorial**: Calculates the factorial of the first number.
- **nCr & nPr**: Calculates combinations and permutations.
- **Logarithms**: Supports both `log10` and `ln`.
- **Trigonometry**: Supports sin, cos, and tan operations.

## Code Structure

- **Main class `Calculator`**: Manages the creation of the interface and the implementation of operations.
- **Methods**:
  - `Add()`, `Subtraction()`, `Multiply()`, `Divide()`: Perform basic arithmetic.
  - `Combination()`, `Permutation()`: Handle combinatorial calculations.
  - `sin()`, `cos()`, `tan()`: Calculate trigonometric values.
  - `log10()`, `LogE()`: Perform logarithmic operations.

## Future Enhancements

- Add error handling for edge cases like dividing by zero.
- Enhance the UI for better user experience.
- Add more advanced functions like hyperbolic trigonometry.

## Author

Name - Vineet Sharma
email - mastergenos228@gmail.com

---

This README gives a concise overview of the project and should help others understand how to use the calculator. Let me know if you'd like to modify or add more details!
