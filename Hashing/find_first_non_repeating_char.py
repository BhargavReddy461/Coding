a = input()
n = len(a)


def firstnonrepeating(arr, n):

    data_count = {}
    data_index = {}

    for i in range(n):
        if arr[i] in data_count:
            data_count[arr[i]] += 1
        else:
            data_count[arr[i]] = 1
            data_index[arr[i]] = i
    for i in range(n):
        if data_count[arr[i]] == 1:
            return arr[data_index[arr[i]]]

    else:
        return -1


print(firstnonrepeating(a, n))
