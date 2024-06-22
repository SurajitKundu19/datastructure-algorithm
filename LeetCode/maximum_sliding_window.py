from collections import deque

arr = [1, 2, 2, 3, 1, 6, 8, 1]
k = 3


def insert_dqueue(i, q):
    while q and arr[i] >= arr[q[-1]]:
        q.pop()
    q.append(i)


def max_sliding_window():
    output = []
    q = deque()
    for i in range(k):
        insert_dqueue(i, q)

    output.append(arr[q[0]])

    for idx in range(k, len(arr)):
        insert_dqueue(idx, q)
        output.append(arr[q[0]])
    print(output)
    return output


max_sliding_window()
