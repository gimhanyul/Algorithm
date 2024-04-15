def lcs(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # LCS 문자열 추출
    lcs_length = dp[n][m]
    lcs_str = ""
    i, j = n, m
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs_str = s1[i-1] + lcs_str
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    return lcs_length

s1 = input()
s2 = input()
print(lcs(s1, s2))