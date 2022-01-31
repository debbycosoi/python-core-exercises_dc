
import string

class Exercises:

    def exercise1(self, stri):
        ''' Count all letters, digits, and special symbols from a given string  '''
        chars = 0
        digits = 0
        symbols = 0
        for i in stri:
            if i.isalpha():
                chars +=1
            elif i.isnumeric():
                digits +=1
            else:
                symbols+=1
        return chars, digits, symbols

    def editDistance(self, str1, str2, m, n):
        if m == 0:
            return n 
        if n == 0:
            return m
        if str1[m-1] == str2[n-1]:
            return editDistance(str1, str2, m-1, n-1)

        return 1 + min(editDistance(str1, str2, m, n-1),   
                    editDistance(str1, str2, m-1, n),    
                    editDistance(str1, str2, m-1, n-1)    
                    )

if __name__ == '__main__':
    exe = Exercises()
    print(exe.exercise1("P@#yn26at^&i5ve"))
    print(exe.editDistance("sunday", "saturday", len("sunday"), len("saturday")))