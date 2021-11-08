def edit_distance_alignment(str1, str2):
    str1 = "-" + str1
    str2 = "-" + str2

    score_mat = [[0 for i in range(len(str2))] for j in range(len(str1))]
    backtrack_mat = [[None for i in range(len(str2))] for j in range(len(str1))]

    for i in range(len(str2)):
        score_mat[0][i] = i
        backtrack_mat[0][i] = "l"

    for j in range(len(str1)):
        score_mat[j][0] = j
        backtrack_mat[j][0] = "u"

    for i in range(1, len(str2)):
        for j in range(1, len(str1)):
            score1 = score_mat[j - 1][i - 1] + (0 if str1[j] == str2[i] else 1)
            score2 = score_mat[j - 1][i] + 1
            score3 = score_mat[j][i - 1] + 1
            score_mat[j][i] = min(score1, score2, score3)
            if score_mat[j][i] == score1:
                backtrack_mat[j][i] = "d"
            elif score_mat[j][i] == score2:
                backtrack_mat[j][i] = "u"
            elif score_mat[j][i] == score3:
                backtrack_mat[j][i] = "l"

    j = len(str1) - 1
    i = len(str2) - 1
    aligned_1 = ""
    aligned_2 = ""
    while i != 0 or j != 0:
        direction = backtrack_mat[j][i]
        if direction == "d":
            aligned_1 = str1[j] + aligned_1
            aligned_2 = str2[i] + aligned_2
            i -= 1
            j -= 1
        elif direction == "u":
            aligned_1 = str1[j] + aligned_1
            aligned_2 = "-" + aligned_2
            j -= 1
        else:
            aligned_1 = "-" + aligned_1
            aligned_2 = str2[i] + aligned_2
            i -=1

    return score_mat[len(str1) - 1][len(str2) - 1], aligned_1, aligned_2