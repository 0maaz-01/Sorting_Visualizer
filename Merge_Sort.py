import time

def merge_sort(data, draw_on_screen, time_gap):
    merge_sort_algo(data, 0, len(data)-1, draw_on_screen, time_gap)

def merge_sort_algo(data, left, right, draw_on_screen, time_gap):
    if left < right:
        middle = (left+right)//2
        merge_sort_algo(data, left, middle, draw_on_screen, time_gap)
        merge_sort_algo(data, middle+1, right, draw_on_screen, time_gap)
        merge(data, left, middle, right, draw_on_screen, time_gap)

def merge(data, left, middle, right, draw_on_screen, time_gap):
    draw_on_screen(data, colors(len(data), left, middle, right))
    time.sleep(time_gap)
    left_part = data[left : middle+1]
    right_part = data[middle+1 : right+1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right + 1):  # Include the 'right' boundary here
        if leftIdx < len(left_part) and rightIdx < len(right_part):
            if left_part[leftIdx] <= right_part[rightIdx]:
                data[dataIdx] = left_part[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = right_part[rightIdx]
                rightIdx += 1
        elif leftIdx < len(left_part):
            data[dataIdx] = left_part[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = right_part[rightIdx]
            rightIdx += 1
    draw_on_screen(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))] )
    time.sleep(time_gap)


def colors(length, left, middle, right):
    colors = []
    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colors.append("yellow")
            else:
                colors.append("orange")
        else:
            colors.append("white")
    return colors