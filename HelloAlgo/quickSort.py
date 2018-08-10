def quickSort(array):
    if len(array) < 2:
        return array

    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i >= pivot]

        return quickSort(less) + [pivot] + quickSort(greater)


print(quickSort([10, 5, 2, 3]))


def quickSort_2(array):
    if len(array) < 2:
        return array

    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i >= pivot]

        return quickSort_2(less) + [pivot] + quickSort_2(greater)


print(quickSort_2([10, 5, 2, 3]))