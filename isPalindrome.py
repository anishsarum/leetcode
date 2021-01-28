class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        revX = strX [::-1]
        pal = True
        
        for i in range(0, len(strX)//2):
            if strX[i] != revX[i]:
                pal = False
        
        return pal
