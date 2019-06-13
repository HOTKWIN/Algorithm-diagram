#分而治之，D&C
class parctice(object):

    def sum_DC(self,arr):
        if len(arr) == 0:
            return 0
        elif len(arr) == 1:
            return arr[0]
        else:
            tmp = arr.pop(0)
            return tmp+self.sum_DC(arr)

    def numOfList_DC(self,arr):
        if len(arr) == 0:
            return 0
        else:
            arr.pop(0)
            return 1+self.numOfList_DC(arr)

    def maxOfList_DC(self,arr):
        if len(arr) == 0:
            return 0
        elif len(arr) == 1:
            return arr[0]
        else:
            if arr.pop(0) < self.maxOfList_DC(arr):
                return self.maxOfList_DC(arr)

    def binary_search(self,arr,item):
        if len(arr) == 0:
            return None
        elif len(arr) == 1:
            return 0
        else:
            if arr[len(arr)//2] == item:
                return len(arr)//2
            elif arr[len(arr)//2] < item:
                arr = arr[len(arr)//2+1:]
                return self.binary_search(arr,item)
            else:
                arr = arr[:len(arr)//2]
                return self.binary_search(arr,item)


#快速排序
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array if i <pivot]
        greater = [i for i in array if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    test = parctice()
    print(test.sum_DC([1,5,8,19]))
    print(test.numOfList_DC(([1,5,8,19])))
    print(test.maxOfList_DC([1,5,8,19]))
    print(test.binary_search([1,5,8,19],8))
    print(quicksort([7,1,6,78]))