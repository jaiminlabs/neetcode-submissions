class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # If lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        # Count frequency of characters in s
        for c in s:
            if c in countS:
                countS[c] += 1
            else:
                countS[c] = 1

        # Count frequency of characters in t
        for c in t:
            if c in countT:
                countT[c] += 1
            else:
                countT[c] = 1

        # Compare the frequency dictionaries
        return countS == countT
   

        

         
