# Static Code Analysis – Findings and Fixes

| No. | Tool | Issue | Severity / Type | Fix Applied |
|---|---|---|---|---|
| 1 | Bandit | Use of `eval()` | Medium | Removed dynamic evaluation and used direct numeric calculations. |
| 2 | Bandit | Use of MD5 hashing | High | Replaced MD5 with SHA-256. |
| 3 | Bandit | Insecure random number generation | Low | Used Python's `secrets` module to generate the checkout PIN securely. |
| 4 | Bandit | Shell command execution | High | Removed unsafe shell command execution. |
| 5 | Bandit | Broad exception handling with `pass` | Low | Removed unnecessary exception suppression. |
| 6 | Pylint | Missing docstrings and naming issues | Code quality | Added docstrings and improved function naming and documentation. |
| 7 | Pylint | Mutable default argument | Code quality | Replaced the mutable default list with `None` and initialized it inside the function. |
| 8 | Flake8 | Unused imports and variables | Style | Removed unused imports and variables. |
| 9 | Flake8 | Lines exceeding the maximum length | Style | Split long statements across multiple lines. |
| 10 | Flake8 | Missing final newline | Style | Ensured the file ends with a newline. |

## Conclusion

Static analysis tools helped identify security vulnerabilities, code-quality problems, and formatting violations. The code was updated to address these findings, and the tools were run again to verify the improvements.