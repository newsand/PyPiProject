import sympy
import requests


def isPalindrome(str):
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


def get_pi_cases(current_digit, batch_size) -> str:
    x = requests.get("https://api.pi.delivery/v1/pi?start={}&numberOfDigits={}".format(current_digit, batch_size))
    'pega as proximas casas de pi'

    return (x.json()['content'])


def get_palindrome_prime(number_size, pi) -> str:
    for n in range(0, len(pi) - number_size):
        if sympy.isprime(int(pi[n:n + number_size])):
            if isPalindrome(pi[n:n + number_size]):
                # print('ISPALINDROME')
                # print('is', pi[n:n + number_size], 'is prime? ', sympy.isprime(int(pi[n:n + number_size])))
                return (pi[n:n + number_size])
    return ''


if __name__ == "__main__":
    number_size = 9
    batch_size = 1500
    found = False
    current_digit = 0
    while not found:
        print(current_digit)
        pi = get_pi_cases(current_digit, batch_size)
        # print(pi)
        current_digit = current_digit + batch_size - number_size
        palindrome = get_palindrome_prime(number_size, pi)
        if palindrome:
            print("first palindrome prime is: ", palindrome)
            print('digito:', current_digit)
            found = True
