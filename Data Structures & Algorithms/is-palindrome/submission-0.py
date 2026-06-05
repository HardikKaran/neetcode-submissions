class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(char for char in s if char.isalnum())
        
        return clean.lower() == clean[::-1].lower()