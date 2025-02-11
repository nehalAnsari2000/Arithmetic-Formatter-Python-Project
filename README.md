# Arithmetic Formatter (Python)

## Description
The Arithmetic Formatter is a Python project designed to format and arrange simple arithmetic problems involving addition and subtraction. This project was created as part of the **'Scientific Computing with Python' certification on FreeCodeCamp** and was a mandatory task to complete the certification.

This program takes a list of arithmetic problems (addition and subtraction) and arranges them in a structured format similar to how arithmetic problems are traditionally presented in schools. Additionally, it provides an option to display the results of the calculations.

---

## Features
- Accepts up to **five** arithmetic problems at a time.
- Supports **addition (+)** and **subtraction (-)** operations.
- Ensures that numbers contain **only digits** (no letters or special characters).
- Limits numbers to a **maximum of four digits**.
- Properly formats problems in a **vertically aligned layout**.
- Displays answers when an optional argument is provided.
- Returns **error messages** for invalid input.

---

## Usage

### Function Definition
```python
arithmetic_arranger(problems, show_answers=False)
```

### Parameters
- **problems**: A list of arithmetic problems as strings (maximum 5 problems allowed).
- **show_answers**: A boolean flag (**True/False**) to display the results of the arithmetic operations. Default is `False`.

### Example Usage
```python
from arithmetic_formatter import arithmetic_arranger

# Example problems
problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]

# Without answers
print(arithmetic_arranger(problems))

# With answers
print(arithmetic_arranger(problems, True))
```

### Expected Output
Without answers:
```
   32       1    9999    523
 +  8  - 3801  + 9999  -  49
 ----  ------  ------  -----
```

With answers:
```
  32       1    9999    523
+  8  - 3801  + 9999  -  49
----  ------  ------  -----
  40   -3800   19998    474
```

---

## Error Handling
The program returns an error message if:
- More than **five problems** are provided.
- An **operator other than + or -** is used.
- **Non-numeric characters** are found in operands.
- An operand contains **more than four digits**.

### Example Errors
```python
print(arithmetic_arranger(["12345 + 6789"]))
# Output: "Error: Numbers cannot be more than four digits."

print(arithmetic_arranger(["32 * 8"]))
# Output: "Error: Operator must be '+' or '-'."
```

---

## Certification
This project was developed as a requirement for the **'Scientific Computing with Python' certification on FreeCodeCamp**. It demonstrates Python programming skills, including string manipulation, validation, and formatting.

---


