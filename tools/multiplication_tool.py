# tools/multiplication_tool.py
from typing import List

class MultiplicationTool:
    """A tool for multiplying a list of numbers.

    This class provides functionality to multiply multiple integers together.

    Methods:
        multiply(numbers): Multiplies a list of integers.
    """
    def multiply(self, numbers: List[int]) -> int:
        """Multiplies a list of numbers.

        Args:
            numbers (List[int]): A list of integers to be multiplied.

        Returns:
            int: The product of the input numbers.

        Raises:
            ValueError: If the input list is empty.
        """
        if not numbers:
            raise ValueError("The input list must not be empty.")
        result = 1
        for number in numbers:
            result *= int(number)
        return result
