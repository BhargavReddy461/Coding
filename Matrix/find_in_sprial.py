# Python3 program for Kth element in spiral
# form of matrix
MAX = 100

''' function for Kth element '''


def findK(A, n, m, k):

    if (n < 1 or m < 1):
        return -1

    '''....If element is in outermost ring ....'''
    ''' Element is in first row '''
    if (k <= m):
        return A[0][k - 1]

    ''' Element is in last column '''
    if (k <= (m + n - 1)):
        return A[(k - m)][m - 1]

    ''' Element is in last row '''
    if (k <= (m + n - 1 + m - 1)):
        return A[n - 1][m - 1 - (k - (m + n - 1))]

    ''' Element is in first column '''
    if (k <= (m + n - 1 + m - 1 + n - 2)):
        return A[n - 1 - (k - (m + n - 1 + m - 1))][0]

    '''....If element is NOT in outermost ring ....'''
    ''' Recursion for sub-matrix. &A[1][1] is 
	address to next inside sub matrix.'''
    A.pop(0)
    [j.pop(0) for j in A]
    return findK(A, n - 2, m - 2, k - (2 * n + 2 * m - 4))


''' Driver code '''

a = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]]
k = 17
print(findK(a, 3, 6, k))

# This code is contributed by shivanisinghss2110
