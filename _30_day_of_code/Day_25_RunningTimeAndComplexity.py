from model_linkedlist.node import Node


class Solution:
    def detectPrime(self, n):
        if n < 2:
            print("Not prime")
            return

        i = 2
        while i * i <= n:
            if n % i == 0:
                print("Not prime")
                return
            i += 1

        print("Prime")


if True:
    s = Solution()
    n = 12
    s.detectPrime(n)

if True:
    s = Solution()
    n = 5
    s.detectPrime(n)

if True:
    s = Solution()
    n = 7
    s.detectPrime(n)

if True:
    s = Solution()
    n = 1
    s.detectPrime(n)

