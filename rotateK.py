'''Problem Statement: Given an array of n size, rotate the array by k elements using the Block Swap Algorithm.

Examples:

Example 1:
Input: N = 5, array[] = {1,2,3,4,5} K=2
Output: {3,4,5,1,2}
Explanation: Rotate the array to right by 2 elements.

Example 2:
Input: N = 7, array[] = {1,2,3,4,5,6,7} K=3
Output: {4,5,6,7,1,2,3}
Explanation: Rotate the array to right by 3 elements.'''

def rotate(arr,k):
    k = k % len(arr)
    l , r = 0 , len(arr)-1
    while l < r:
        arr[l] ,arr[r] = arr[r] , arr[l]
        l += 1
        r -= 1
    l , r = 0 , k-1
    while l < r:
        arr[l] ,arr[r] = arr[r] , arr[l]
        l += 1
        r -= 1
    l , r = k , len(arr)-1
    while l < r:
        arr[l] ,arr[r] = arr[r] , arr[l]
        l += 1
        r -= 1
    print(arr)


if __name__ == '__main__':
    arr = list(map(int , input("Enter array: ").strip('[]').split(',')))
    k = int(input("Enter K Value: "))
    rotate(arr,k)