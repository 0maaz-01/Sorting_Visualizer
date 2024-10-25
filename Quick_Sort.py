import time

def partition(data_list, head, tail, draw_on_screen, time_gap):
    border = head
    pivot = data_list[tail]

    draw_on_screen(data_list, colors(len(data_list), head, tail, border, border))
    time.sleep(time_gap)

    for j in range(head, tail):
        if (data_list[j] < pivot):
            draw_on_screen(data_list, colors(len(data_list), head, tail, border, j, True))
            time.sleep(time_gap)
            data_list[border], data_list[j] = data_list[j], data_list[border]
            border += 1
        draw_on_screen(data_list, colors(len(data_list), head, tail, border, j, True))
        time.sleep(time_gap)

    draw_on_screen(data_list, colors(len(data_list), head, tail, border, tail, True))
    time.sleep(time_gap)
    data_list[border], data_list[tail] = data_list[tail], data_list[border]
    return border

def quick_sort(data_list, head, tail, draw_on_screen,time_gap):
    if head < tail:
        partitionIdx = partition(data_list, head, tail, draw_on_screen, time_gap)

        quick_sort(data_list, head, partitionIdx-1, draw_on_screen, time_gap)

        quick_sort(data_list, partitionIdx+1, tail, draw_on_screen, time_gap)


def colors(len_data, head, tail, border, current_index, isSwapping = False):
    colors = []

    for index in range(len_data):
        if index >= head and index <= tail:
            colors.append("gray")
        else:
            colors.append("white")

        if index == tail:
            colors[index] = "orange"
        elif index == border:
            colors[index] = "red"
        elif index == current_index:
            colors[index] = "yellow"

        if isSwapping:
            if index == border or index == current_index:
                colors[index] = "green"
    return colors