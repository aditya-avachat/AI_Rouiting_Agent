# tools/multiplication_tool.py
from typing import List

class MultiplicationTool:
    def multiply(self, numbers: List[int]) -> int:
        """Multiplies a list of numbers."""
        result = 1
        for number in numbers:
            result *= number
        return result
