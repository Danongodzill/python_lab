Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> try:
...     a = float(input("A: "))
...     b = float(input("B: "))
...     operation = input("Операція (+, -, *, /): ").strip()
... 
...     if operation == "+":
...         result = a + b
...     elif operation == "-":
...         result = a - b
...     elif operation == "*":
...         result = a * b
...     elif operation == "/":
...         if b == 0:
...             raise ZeroDivisionError("на нуль ділити не можна.")
...         result = a / b
...     else:
...         raise ValueError(f"невідома операція '{operation}'.")
... 
...     print("Результат:", result)
... except ValueError as error:
...     print("Помилка:", error if str(error).startswith("невідома") else "потрібно ввести коректні числа.")
... except ZeroDivisionError as error:
