class VowelCounter:
    def count_vowels(self, text: str) -> int:
        """Counts the number of vowels in a given string.

        Args:
            text (str): The input string to count vowels in.

        Returns:
            int: The total number of vowels found in the input string.
        """
        vowels = "aeiouAEIOU"
        return sum(1 for char in text if char in vowels)