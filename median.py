'''Problem Statement: Given an unsorted array, find the median of the given array.

Examples:

Example 1:
Input: [2,4,1,3,5]
Output: 3

Example 2:
Input: [2,5,1,7]
Output: 3.5
What is a Median?
Median is defined as the value which is present in the middle for a series of values. Note, in order to find the median of an array of integers, we must make sure they are sorted.'''


def median(arr):
    n = len(arr)
    arr.sort()
    res = 0
    if n % 2 == 0:
        i=int(n/2)
        res = (arr[i]+arr[i-1])/2

    else:
        i = int(n/2)
        res = arr[i]
    print(res)    

if __name__ == '__main__':
    arr = list(map(int , input("Enter array: ").strip('[]').split(',')))
    median(arr)