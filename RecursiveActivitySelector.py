# Note that this algorithm assumes that first activity is already selected at first (i.e. k = 0)
def recursive_activity_selector(s, f, k, n):
    m = k + 1
    while m <= n and s[m] < f[k]:
        m += 1
    if m <= n:
        return [m + 1] + recursive_activity_selector(s, f, m, n)
    else:
        return []


if __name__ == "__main__":
    start_times = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    finish_times = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    n = len(start_times) - 1

    result_indices = recursive_activity_selector(
        start_times, finish_times, 0, n)

    print("Activity Detail:\n\n", start_times, "\n", finish_times)
    print("\nSelected activities are ", result_indices, " index, which is:")
    selected_activities = [[start_times[i - 1], finish_times[i-1]]
                           for i in result_indices]

    for activity in selected_activities:
        print("\tStart time:", activity[0], "| End time:", activity[1])
    print("\n")
