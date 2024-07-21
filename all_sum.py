'''Problem Statement: Given an array, we have to find the sum of all the elements in the array.

Examples:

Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: 15
Explanation: Sum of all the elements is 1+2+3+4+5 = 15

Example 2:
Input:  N=6, array[] = {1,2,1,1,5,1}
Output: 11
Explanation: Sum of all the elements is 1+2+1+1+5+1 = 11'''

def all_sum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    print(sum)
if __name__ == '__main__':
    arr = list(map(int , input().strip('[]').split(',')))
    all_sum(arr)