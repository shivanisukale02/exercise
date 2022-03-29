def prime(x):
    if (x%2!=0) & (x%3!=0) & (x%5!=0) & (x%7!=0):
        return True
    else:
        return False


def Palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

if __name__=="__main__":
    n1=input()
    result=prime(n1)
    result2=Palindrome(n1)
