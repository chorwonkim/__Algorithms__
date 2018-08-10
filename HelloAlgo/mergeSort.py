def merge(left, right):
    result = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]

    return result


def mergeSort(myList):

    if len(myList) <= 1:
        return myList

    mid = len(myList) // 2

    leftList = myList[:mid]
    rightList = myList[mid:]

    leftList = mergeSort(leftList)
    rightList = mergeSort(rightList)

    return merge(leftList, rightList)


x = [6, 3, 2, 8, 1, 4, 7, 5]
print(mergeSort(x))


def mergeSort2(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    leftList = array[:mid]
    rightList = array[mid:]

    leftList = mergeSort2(leftList)
    rightList = mergeSort2(rightList)

    return merge(leftList, rightList)

x = [6, 3, 2, 8, 1, 4, 7, 5]
print(mergeSort2(x))