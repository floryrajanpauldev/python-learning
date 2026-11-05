# Python Coding Style

## 1. What is PEP 8?

**PEP 8** is the official Python style guide. It defines conventions and recommendations for writing clean, readable, and consistent Python code.

The goal is to make code easier to read, understand, maintain, and share with other developers.

### Common PEP 8 Guidelines

- **Indentation:** Use 4 spaces for each indentation level.
- **Line Length:** Avoid writing very long lines of code that are difficult to read. PEP 8 recommends limiting lines to 79 characters for code.
- **Naming Conventions:** Use descriptive variable and function names. Use `snake_case` for variables and functions.
- **Spacing:** Use appropriate spaces around operators and after commas.
- **Blank Lines:** Use blank lines to separate functions and logical sections of code.
- **Readability:** Write code that is easy for other developers to understand.

## 2. Pylint

**Pylint** is a Python code analysis tool that checks code for errors, coding standard violations, and potential problems.

It helps developers improve code quality and follow good coding practices.

### Installation

Run the following command in your terminal:

```bash
python3 -m pip install pylint
```

### Usage

Run Pylint against a Python file:

```bash
python3 -m pylint style.py
```

Pylint analyzes the file and reports issues and suggestions for improvement.

## 3. pycodestyle

**pycodestyle** is a tool that checks Python code against the PEP 8 style guide.

It identifies style violations such as incorrect indentation, spacing, and line length.

### Installation

```bash
python3 -m pip install pycodestyle
```

### Usage

```bash
python3 -m pycodestyle style.py
```

It reports any PEP 8 style violations found in the file.

## 4. Black – Python Code Formatter

**Black** is an automatic Python code formatter.

Instead of manually fixing formatting issues, Black automatically reformats your Python code according to its formatting rules, which are largely aligned with PEP 8.

### Installation

Run the following command:

```bash
python3 -m pip install black
```

### Usage

To format a Python file, run:

```bash
python3 -m black harvard-cs50p/07-coding-style/style.py
```

Black automatically reformats the file to make the code consistent and readable.

## 5. Difference Between Pylint, pycodestyle, and Black

| Tool | Purpose |
|---|---|
| **Pylint** | Analyzes code for errors, potential issues, and coding standard violations |
| **pycodestyle** | Checks whether code follows PEP 8 style guidelines |
| **Black** | Automatically formats Python code |

## 6. Key Takeaways

- **PEP 8** defines Python coding style conventions.
- **Pylint** analyzes code quality and identifies potential problems.
- **pycodestyle** checks code against PEP 8.
- **Black** automatically formats Python files.
- Following coding standards makes code easier to read, maintain, and collaborate on.

**Remember:** Writing code that works is important, but writing code that is clean, consistent, and readable is equally important.