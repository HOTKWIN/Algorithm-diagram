"""
二分查找
O(log2n)
"""


def binary_search(list,item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


if __name__ == '__main__':
    list1 = [1,3,5,7,9]
    print(binary_search(list1,3))
    print(binary_search(list1,9))
    print(binary_search(list1,-1))
