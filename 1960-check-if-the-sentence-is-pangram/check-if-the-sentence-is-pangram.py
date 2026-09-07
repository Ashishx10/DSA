import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
        return all(letter in sentence for letter in string.ascii_lowercase)
