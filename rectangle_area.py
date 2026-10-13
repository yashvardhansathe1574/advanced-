"""
Program    : Calculate the Area of a Rectangle

Description:
    This program accepts the length and breadth of a rectangle
    from the user and calculates its area.

Formula:
    Area = Length × Breadth

Input:
    Length of the rectangle
    Breadth of the rectangle

Output:
    Area of the rectangle

Approach:
    1. Accept the length and breadth from the user.
    2. Store the values as instance variables.
    3. Calculate the area using the formula:
           Area = Length × Breadth
    4. Display the calculated area.

Author:
    CRD
"""


class Area:
    """
    A class to calculate the area of a rectangle.
    """

    def __init__(self):
        """
        Initialize the rectangle dimensions.
        """
        self.length = float(input("Enter length  : "))
        self.breadth = float(input("Enter breadth : "))

    def calculate_area(self):
        """
        Calculate and display the area of the rectangle.

        Returns:
            float: Area of the rectangle.
        """
        area = self.length * self.breadth
        print(f"\nArea of Rectangle = {area}")
        return area


if __name__ == "__main__":
    rectangle = Area()
    rectangle.calculate_area()
