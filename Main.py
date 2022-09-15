def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True

def get_pi_cases(file):
  pass


if __name__=="__main__":
  
  for n in range(0,len(pi)-21):
      if sympy.isprime(int(pi[n:n + 21])):
          if isPalindrome(pi[n:n + 21]):
              print('ISPALINDROME')
          print('is',pi[n:n+21],'is prime? ',sympy.isprime(int(pi[n:n+21])))
           
