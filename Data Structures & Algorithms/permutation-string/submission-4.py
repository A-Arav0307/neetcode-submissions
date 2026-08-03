class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        frequency_s1 = {}

        def frequency(string):
            frequency = {}
            for c in string:
                if c not in frequency:
                    frequency[c] = 0
                frequency[c] += 1
            return frequency

        def valid(f1, f2):
            for c in f1:
                if c not in f2 or f1[c] != f2[c]:
                    return False

            return True 

        frequency_s1 = frequency(s1)

        i = 0
        while i < len(s2):
    
            if s2[i] not in frequency_s1:
                i+= 1
            elif i + len(s1) - 1 <= len(s2):
                new_string = s2[i:i+len(s1)]
                frequency_s2 = frequency(new_string)
                if valid(frequency_s1, frequency_s2): return True
                i += len(s1) - 1

            else:
                i += 1
                  


        if i == len(s2):
            return False 

    