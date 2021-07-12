import sys

sys.setrecursionlimit(10000)


def passwordCracker(passwords, loginAttempt):
    memo = set()
    res = []
    crack(loginAttempt, passwords, res, memo)
    return ' '.join(res) if len(res) > 0 else "WRONG PASSWORD"


def crack(password, keys, res, memo):
    if len(password) == 0:
        return True

    if password in memo:
        return False

    for key in keys:
        if password[:len(key)] == key:
            res.append(key)
            memo.add(password)

            if crack(password[len(key):], keys, res, memo):
                return True

            del res[-1]

    return False


def runTestCase(fileName):
    f = open(fileName, 'r')

    t = int(f.readline().strip())
    for _ in range(0, t):
        f.readline()
        passwords = list(f.readline().strip().split())
        loginAttempt = f.readline().strip()
        result = passwordCracker(passwords, loginAttempt)
        print(result)


if True:
    passwords = ["abra", "ka", "dabra"]
    loginAttempts = 'abrakadabra'

    result = passwordCracker(passwords, loginAttempts)
    print("Result ", result)

if True:
    passwords = ["abra", "ka", "dabra"]
    loginAttempts = 'kaabra'

    result = passwordCracker(passwords, loginAttempts)
    print("Result ", result)

if True:
    passwords = ["gurwgrb", "maqz", "holpkhqx", "aowypvopu"]
    loginAttempts = 'gurwgrb'

    result = passwordCracker(passwords, loginAttempts)
    print("Result ", result)

if True:
    passwords = ["ab", "abcd", "cd"]
    loginAttempts = 'abcd'

    result = passwordCracker(passwords, loginAttempts)
    print("Result ", result)

if True:
    #Forth test case runs out time without memoization
    runTestCase('../_in/problem_solving/_11_recursion/PasswordCracker_TestCase2')
    print()
