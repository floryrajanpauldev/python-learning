# Python Debugging

## 1. What is Debugging?

Debugging is the process of finding and fixing errors in a program.

Instead of simply running a Python file and looking at the final output, we can use a debugger to understand how the code executes step by step.

## 2. Debugging in VS Code

Visual Studio Code (VS Code) provides a built-in debugging feature that allows us to pause program execution, inspect variables, and follow the flow of our code.

### Steps to Debug a Python Program

1. Open your Python file in VS Code.
2. Set a **breakpoint** by clicking next to the line number where you want the program to pause. A red dot will appear.
3. Do not just click **Run Python File**. Instead, open the **Run and Debug** option from the left sidebar.
4. Click **Run and Debug** to start debugging.
5. When the program reaches the breakpoint, execution pauses at that line.
6. Use the debugging controls to understand how the program executes.

### Important Debugging Controls

| Control | Purpose |
|---|---|
| Continue | Resumes execution until the next breakpoint or program completion |
| Step Over | Executes the current line and moves to the next line without entering a function |
| Step Into | Enters a function to examine its internal execution |
| Step Out | Finishes the current function and returns to the calling code |
| Restart | Restarts the debugging session |
| Stop | Stops the debugging session |

### Inspecting Variables

While debugging, look at the **Variables** section in the left panel.

It displays:
- Variable names.
- Current variable values.
- How variable values change as the program executes.

This helps us understand what is happening inside our program.

## 3. Example: Debugging a Pyramid

When printing a pyramid, debugging helps us understand how loops and conditions work.

For example, consider this condition:

```python
if i == 0:
    print(" ")
else:
    print("#")
```

If `i` starts at `0`, the first brick (`#`) will not print because the condition is true and Python prints a space instead.

If we use `i + 1` in the condition:

```python
if i + 1 == 0:
    print(" ")
else:
    print("#")
```

The first brick will print because when `i` is `0`, `i + 1` equals `1`, so the condition is false.

**Important:** The result depends on the condition and how the loop variable is initialized.

## 4. Key Takeaways

- A breakpoint pauses program execution at a specific line.
- Use **Run and Debug** instead of simply running the Python file.
- **Step Over** and **Step Into** help you follow the code flow.
- The Variables panel shows the current values of variables.
- Debugging helps identify logical errors, not just syntax errors.

**Remember:** Debugging allows you to see what your code is doing while it runs, rather than only seeing the final output.