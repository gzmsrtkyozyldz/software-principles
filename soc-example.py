# Consider a simple program that calculates the area and perimeter of a rectangle.
# We can separate the concerns into two components: the calculation logic and the user interface.
# Calculation Logic:
# Contains functions responsible for performing the calculations.
# Handles the mathematical operations and returns the results.
# Example code:
# calculation_logic.py
def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)
# User Interface:
# Handles user input and output.
# Calls the appropriate functions from the calculation logic component.
# Example code:
# user_interface.py
import calculation_logic # bak tekrar


def get_user_input():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    return length, width


def display_results(area, perimeter):
    print(f"The area of the rectangle is: {area}")
    print(f"The perimeter of the rectangle is: {perimeter}")


def main():
    length, width = get_user_input()
    area = calculation_logic.calculate_area(length, width)
    perimeter = calculation_logic.calculate_perimeter(length, width)
    display_results(area, perimeter)

    main()
# In this example, the calculation logic component focuses solely on performing the area and perimeter calculations,
# while the user interface component handles user input and output.
# This separation allows for easier maintenance and reusability of the code.
# The calculation logic can be reused in other parts of the program or in different programs altogether,
# while the user interface can be modified or replaced without affecting the underlying calculations.

# By adhering to the SoC principle, you can enhance the modularity and maintainability of your code,
# making it easier to understand, test, and extend in the future.
