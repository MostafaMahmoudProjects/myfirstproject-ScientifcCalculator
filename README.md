# Scientific Calculator

A Python desktop calculator with a dark CustomTkinter keypad and a hand-written expression evaluator. It’s a work in progress. You can calculate the sine of an angle in degrees or radians, take logarithms, and work with powers and constants. Basic arithmetic and compound expressions still have some surprising edge cases.

## Try it

The calculator starts in degree mode. Click **sin**, type `30)`, and press **Enter** to get `0.5`. Click **DEG** to switch to radians. Use the keypad for scientific functions and the constants π and e. The keyboard accepts numbers, decimal points, arithmetic operators, and parentheses.

| Expression | Angle mode | Result |
| --- | --- | --- |
| `sin(π/6)` | RAD | `0.5` |
| `cos(60)` | DEG | `0.5` |
| `tan(45)` | DEG | `1.0` |
| `log(100)` | Either | `2.0` |
| `ln(1)` | Either | `0.0` |
| `2^3^2` | Either | `512.0` |
| `2π` | Either | `6.283185307179586` |

The display keeps the last three successful calculations for the session. Use the copy button to copy the displayed value, **Backspace** to delete the last input, or **Escape** to clear the current expression.

## How it works

- **`main.py`** builds the desktop interface with CustomTkinter on top of Tkinter. It handles button presses, keyboard input, angle mode, the clipboard, and history.
- **`calculator.py`** exposes `solve(expression, angle_mode)`. It processes expression strings in Python and uses the standard library’s `math` module for constants, trigonometry, and logarithms.

## Current limitations

- Some basic arithmetic fails. For example, `12/3` returns `4.0`, but `9-4` and `2+3*4` return a fallback message.
- Grouping and nested functions are incomplete. Both `(2+3)*4` and `sin(cos(0))` return a syntax error. The natural logarithm accepts a numeric argument such as `ln(1)`, but `ln(e)` also returns a syntax error.
- The square-root button inserts `sqrt(`, but evaluating `sqrt(9)` returns the expression itself. The **2nd** button is disabled.

## Run on Linux

Use a graphical desktop with Python 3, Tkinter, and the Python venv module installed. From the repository root, create a fresh environment and start the app:

```bash
python3 -m venv .venv-local
source .venv-local/bin/activate
python -m pip install customtkinter==6.0.0
python main.py
```
