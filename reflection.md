# Reflection – Static Code Analysis

**1. What did you learn from static code analysis?**

I learned that static code analysis can identify potential security vulnerabilities, coding mistakes, unused variables, and formatting problems without executing the program.

**2. Why are multiple static analysis tools useful?**

Different tools identify different types of problems. Bandit focuses on security, Pylint checks code quality and maintainability, and Flake8 detects style and formatting violations. Using all three provides more comprehensive feedback.

**3. What improvements were made to the code?**

I replaced unsafe evaluation and weak hashing, used secure random number generation, removed unsafe shell execution, corrected exception handling, improved documentation, and fixed formatting issues.

**4. What is the importance of running the tools again after fixing the code?**

Running the tools again verifies whether the reported issues have been resolved and helps confirm that the updated code meets the expected quality and security standards.