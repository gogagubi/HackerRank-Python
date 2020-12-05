class Solution:
    def logic(self, returned, expected):
        returned = list(map(lambda x: int(x), returned))
        expected = list(map(lambda x: int(x), expected))

        if returned[2] <= expected[2]:
            if returned[1] <= expected[1] or returned[2] < expected[2]:
                if returned[0] <= expected[0] or returned[1] < expected[1] or returned[2] < expected[2]:
                    print(0)
                else:
                    print(15 * (returned[0] - expected[0]))
            else:
                print(500 * (returned[1] - expected[1]))
        else:
            print(10000)


if False:
    s = Solution()
    returned = [9, 6, 2015]
    expected = [6, 6, 2015]

    print("Result ")
    s.logic(returned, expected)

if True:
    s = Solution()
    returned = [31, 12, 2009]
    expected = [1, 1, 2010]

    print("Result ")
    s.logic(returned, expected)
