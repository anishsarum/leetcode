class Solution:
    def reverse(self, x: int) -> int:
        xStr = str(x)
        new = ""
        
        for i in range(len(xStr)-1,-1,-1):
            new += xStr[i]
            
        return new
