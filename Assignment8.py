"""
Program: Sequence Number Generator

Description:
    This program generates and displays a sequence of numbers from a
    user-specified starting number up to 100. It also validates the
    input provided by the user.

Input:
    Starting number (integer)

Output:
    Displays the sequence of numbers from the starting number to 100.

Author: CRD
"""


class SequenceGenerator:
    """
    A class to generate and display a sequence of numbers.
    """

    def no_generator(self, start=0, end=100):
        """
        Generate and display numbers from the given starting number to 100.

        Args:
            start (int, optional): The starting number of the sequence.
                Defaults to 0.
            end (int, optional): The ending number of the sequence.
                Defaults to 100.

        Returns:
            None
        """

        if start > end:
            print("Starting number must be less than or equal to 100.")
            return

        for number in range(start, end + 1):
            print(number, end=" ")

    def input_start(self):
        """
        Accept the starting number from the user and generate the sequence.

        Prompts the user to enter an integer and displays numbers from
        the entered value up to 100.

        Returns:
            None
        """

        try:
            start_no = int(input("Enter Start No: "))

            if start_no < 0:
                print("Please enter a positive number.")
            elif start_no > 100:
                print("Starting number cannot be greater than 100.")
            else:
                self.no_generator(start=start_no)

        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    """
    Program execution starts here.
    """

    sequence_generator = SequenceGenerator()
    sequence_generator.input_start()
