class Solution:
    def reverse(self, x: int) -> int:
        xStr = str(x)
        
        if x < 0:
            revStr = -int((xStr[1:])[::-1])
        
        else:
            revStr = int(xStr[::-1])
        
        
        if revStr >= (-2 ** 31) and revStr <= (2 ** 31 - 1):
            return revStr
        
        return 0
