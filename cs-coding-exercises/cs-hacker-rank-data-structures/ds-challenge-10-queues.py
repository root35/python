#!/bin/python3

def win_min_max(arr, win_len):
    if not arr or win_len == 0:
        return []
    
    arr_len = len(arr)
    if win_len > arr_len:
        raise Exception('window_len ({}) is higher than array length ({})'.format(win_len, len(arr)))
    
    if win_len == arr_len:
        return max(arr)

    # Search in the first window
    max_queue = [0]

    for i in range(1, win_len):
        while max_queue and arr[i] > arr[max_queue[-1]]:
            max_queue.pop()
        max_queue.append(i)

    win_min = arr[max_queue[0]]

    # Search in the remaining windows:
    # from (i=win_len) to (len(arr))
    for i in range(win_len, arr_len):
        if i - max_queue[0] >= win_len:
            max_queue.pop(0)
        while max_queue and arr[i] > arr[max_queue[-1]]:
            max_queue.pop()
        max_queue.append(i)
        win_min = min(win_min, arr[max_queue[0]])

    return win_min

# Complete the solve function below.
def solve(arr, queries):
    if not queries or not arr:
        return []

    win_mins = []
    for query in queries:
        win_mins.append(win_min_max(arr, query))
    
    return win_mins

if __name__ == '__main__':

    n, q = map(int, input().strip().split())
    arr = list(map(int, input().rstrip().split()))

    queries = []
    for _ in range(q):
        query = int(input())
        queries.append(query)

    result = solve(arr, queries)
    print('\n'.join([str(r) for r in result if r]))
