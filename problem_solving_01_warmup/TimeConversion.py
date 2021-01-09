def timeConversion(s):
    hour = int(s[0:2])
    suff = s[len(s) - 2:]

    if suff == 'AM' and hour == 12:
        hour = 0
    elif suff == 'PM' and hour != 12:
        hour += 12

    hourStr = str(hour) if hour > 9 else '0' + str(hour)
    ans = hourStr + s[2:len(s) - 2]
    return ans


if True:
    s = "12:01:00PM"

    result = timeConversion(s)
    print("Result ", result)

if True:
    s = "11:59:59PM"

    result = timeConversion(s)
    print("Result ", result)
