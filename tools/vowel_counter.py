# tools/vowel_counter.py

class VowelCounter:
    def count_vowels(self, text: str) -> int:
        """Counts the number of vowels in a given string."""
        vowels = "aeiouAEIOU"
        return sum(1 for char in text if char in vowels)
