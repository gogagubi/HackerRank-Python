import math
import sys


def minimumPasses(m, w, p, n):
    passes = 0
    candy = 0
    spend = sys.maxsize

    while candy < n:
        step = (p - candy) // (m * w)
        if step <= 0:
            resources = candy // p

            gap = min(resources, abs(m - w))
            resources -= gap

            if m > w:
                w += gap
            else:
                m += gap

            m += resources // 2
            w += (resources - (resources // 2))

            candy %= p
            step = 1

        passes += step

        candy += step * m * w
        spend = min(spend, (passes + math.ceil((n - candy) / (m * w))))

    return min(passes, spend)


if True:
    m = 1
    w = 2
    p = 1
    n = 60
    result = minimumPasses(m, w, p, n)
    print("Result ", result)
