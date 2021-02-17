class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check(arr, n):

    maxi = 2147483647
    mini = -2147483648

    flag = True

    for i in range(1, n):
        if arr[i] > arr[i-1] and arr[i] > mini and arr[i] < maxi:
            mini = arr[i-1]
        elif arr[i] < arr[i-1] and arr[i] > mini and arr[i] < maxi:
            maxi = arr[i-1]

        else:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")


arr = [5123, 3300, 783, 1111, 890]
check(arr, len(arr))
