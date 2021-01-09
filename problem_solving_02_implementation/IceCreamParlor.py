def icecreamParlor(m, arr):
    ans = [0] * 2
    nums = {}

    for i in range(0, len(arr)):
        if m - arr[i] in nums:
            ans[0] = nums[m - arr[i]] + 1
            ans[1] = i + 1
            break
        else:
            nums[arr[i]] = i

    return ans


if True:
    m = 4
    arr = [1, 4, 5, 3, 2]

    result = icecreamParlor(m, arr)
    print(result)

if True:
    m = 4
    arr = [2, 2, 4, 3]

    result = icecreamParlor(m, arr)
    print(result)
