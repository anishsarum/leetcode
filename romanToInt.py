class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        s += " "
        
        for i in range(len(s)):
            
            if s[i] == "I":
                
                if s[i+1] == "V":
                    total += 4
                
                elif s[i+1] == "X":
                    total += 9
                
                else:
                    total += 1
            
            elif s[i] == "V" and s[i-1] != "I":
                
                total += 5
                
            elif s[i] == "X" and s[i-1] != "I":
                
                if s[i+1] == "L":
                    total += 40
                
                elif s[i+1] == "C":
                    total += 90
                
                else:
                    total += 10
            
            elif s[i] == "L" and s[i-1] != "X":
                
                total += 50
            
            elif s[i] == "C" and s[i-1] != "X":
                
                if s[i+1] == "D":
                    total += 400
                
                elif s[i+1] == "M":
                    total += 900
                
                else:
                    total += 100
            
            elif s[i] == "D" and s[i-1] != "C":
                
                total += 500
            
            elif s[i] == "M" and s[i-1] != "C":
                
                total += 1000
        
        return total
