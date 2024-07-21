'''roblem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

Examples
Example 1:
Input:
 [1,2,4,7,7,5]
Output:
 Second Smallest : 2
	Second Largest : 5
Explanation:
 The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2

Example 2:
Input:
 [1]
Output:
 Second Smallest : -1
	Second Largest : -1
Explanation:
 Since there is only one element in the array, it is the largest and smallest element present in the array. There is no second largest or second smallest element present.'''

class solution:
    def smallest(arr):
        small = float('inf')
        second_small = float('inf')
        if len(arr) == 1:
            return -1
        for i in range(len(arr)):
            if arr[i] < small:
                second_small = small
                small = arr[i]
            if arr[i] < second_small and arr[i] > small:
                second_small = arr[i]
        return second_small

    def second_largest(arr):
        large = float('-inf')
        second_large = float('-inf')
        if len(arr) == 1:
            return -1
        for i in range(len(arr)):
            if arr[i] > large:
                second_large = large
                large = arr[i]
            if arr[i] > second_large and arr[i] < large:
                second_large = arr[i]
        return second_large




if __name__ == '__main__':
    arr = list(map(int , input().strip('[]').split(',')))
    sol = solution
    print("second_smallest = ",sol.smallest(arr))
    print("second_largest = ",sol.second_largest(arr))
