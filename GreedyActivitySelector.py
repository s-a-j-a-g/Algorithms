def greedy_activity_selector(s, f):
    n = len(s)
    A = [1]  # Select the first activity by default
    k = 0

    for m in range(1, n):
        if s[m] >= f[k]:
            A.append(m + 1)
            k = m

    return A


if __name__ == "__main__":
    start_times = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    finish_times = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    result_indices = greedy_activity_selector(start_times, finish_times)

    print("Activity Detail:\n\n", start_times, "\n", finish_times)

    print("\nSelected activities are ", result_indices, " index, which is:")
    selected_activities = [[start_times[i - 1],   finish_times[i - 1]]
                           for i in result_indices]

    for activity in selected_activities:
        print("\tStart time:", activity[0], "| End time:", activity[1])
    print("\n")
