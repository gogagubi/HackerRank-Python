def abbreviation(a, b):
    dp = []
    for i in range(0, len(b) + 1):
        dp.append([False] * (len(a) + 1))

    dp[0][0] = True

    for i in range(1, len(a)):
        if a[i - 1].islower():
            dp[0][i] = dp[0][i - 1]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if a[j - 1].isupper():
                if a[j - 1] == b[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
            else:
                if a[j - 1].upper() == b[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] or dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

    return "YES" if dp[len(b)][len(a)] is True else "NO"


if True:
    a = 'AbcDE'
    b = 'ABDE'
    result = abbreviation(a, b)
    print("Result ", result)

if True:
    a = 'beFgH'
    b = 'EFG'
    result = abbreviation(a, b)
    print("Result ", result)

if True:
    a = 'DINVMKSOfsVQByBnCWNKPRFRKMhFRSkNQRBVNTIKNBXRSXdADOSeNDcLWFCERZOLQjEZCEPKXPCYKCVKALNxBADQBFDQUpdqunpelxauyyrwtjpkwoxlrrqbjtxlkvkcajhpqhqeitafcsjxwtttzyhzvh'
    b = 'DINVMKSOVQBBCWNKPRFRKMFRSNQRBVNTIKNBXRSXADOSNDLWFCERZOLQEZCEPKXPCYKCVKALNBADQBFDQU'
    result = abbreviation(a, b)
    print("Result ", result)

if True:
    a = 'BFZZVHdQYHQEMNEFFRFJTQmNWHFVXRXlGTFNBqWQmyOWYWSTDSTMJRYHjBNTEWADLgHVgGIRGKFQSeCXNFNaIFAXOiQORUDROaNoJPXWZXIAABZKSZYFTDDTRGZXVZZNWNRHMvSTGEQCYAJSFvbqivjuqvuzafvwwifnrlcxgbjmigkms'
    b = 'BFZZVHQYHQEMNEFFRFJTQNWHFVXRXGTFNBWQOWYWSTDSTMJRYHBNTEWADLHVGIRGKFQSCXNFNIFAXOQORUDRONJPXWZXIAABZKSZYFTDDTRGZXVZZNWNRHMSTGEQCYAJSF'
    result = abbreviation(a, b)
    print("Result ", result)

if True:
    a = 'BFZZVHdQYHQEMNEFFRFJTQmNWHFVXRXlGTFNBqWQmyOWYWSTDSTMJRYHjBNTEWADLgHVgGIRGKFQSeCXNFNaIFAXOiQORUDROaNoJPXWZXIAABZKSZYFTDDTRGZXVZZNWNRHMvSTGEQCYAJSFvbqivjuqvuzafvwwifnrlcxgbjmigkms'
    b = 'BFZZVHQYHQEMNEFFRFJTQNWHFVXRXGTFNBWQOWYWSTDSTMJRYHBNTEWADLHVGIRGKFQSCXNFNIFAXOQORUDRONJPXWZXIAABZKSZYFTDDTRGZXVZZNWNRHMSTGEQCYAJSF'
    result = abbreviation(a, b)
    print("Result ", result)
