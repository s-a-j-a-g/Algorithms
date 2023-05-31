def create_LCS_table(str1, str2):
    m = len(str1)
    n = len(str2)

    # Creating a combined table
    table = [[(" ", 0)] * (n + 1) for _ in range(m + 1)]

    # Filling in the table
    for i in range(1, m + 1):
        table[i][0] = (str1[i-1], 0)
    for j in range(1, n + 1):
        table[0][j] = (str2[j-1], 0)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = ("↖", table[i - 1][j - 1][1] + 1)
            elif table[i - 1][j][1] >= table[i][j - 1][1]:
                table[i][j] = ("↑", table[i - 1][j][1])
            else:
                table[i][j] = ("←", table[i][j - 1][1])

    return table


# Trace back to LCS
def find_LCS(table):
    i = len(table) - 1  # no. of rows = len(str1)
    j = len(table[0]) - 1  # no. of columns = len(str2)
    lcs = ""
    while i > 0 and j > 0:
        direction = table[i][j][0]
        if direction == "↖":
            # equivalent to: lcs = str1[i - 1] + lcs
            lcs = table[i][0][0] + lcs
            i -= 1
            j -= 1
        elif direction == "↑":
            i -= 1
        else:
            j -= 1

    return lcs


if __name__ == "__main__":
    # str1 = "atmosphere"
    # str2 = "stratosphere"
    str1 = input("Enter First String: ")
    str2 = input("Enter Second String: ")

    table = create_LCS_table(str1, str2)
    print("\nTable:")
    for row in table:
        print(row)

    lcs = find_LCS(table)

    print("\nLCS: ", lcs)
