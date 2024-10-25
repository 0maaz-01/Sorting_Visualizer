import time

def selection_sort(data_list, draw_on_screen, time_gap):
    n = len(data_list)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if data_list[j] < data_list[min_index]:
                min_index = j
        data_list[i], data_list[min_index] = data_list[min_index], data_list[i]
        draw_on_screen(data_list, ["blue" if x == i or x == min_index else "red" for x in range(len(data_list))])
        time.sleep(time_gap)
    draw_on_screen(data_list, ["blue" for x in range(len(data_list))])


