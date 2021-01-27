class Solution:
    def reverse(self, x: int) -> int:
        xStr = str(x)
        new = ""
        
        for i in range(len(xStr)-1,-1,-1):
            new += xStr[i]
        
        if x < 0:
            filt = ""
            
            for i in range(len(new)-1):
                filt += new[i]
                
            new = - int(filt)
        
        new = int(new)
        
        if new >= (-2 ** 31) and new <= (2 ** 31 - 1):
            return new
        
        return 0
