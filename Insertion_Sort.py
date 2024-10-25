import time
def insertion_sort(data_list, draw_on_screen, time_gap):
    for i in range(1,len(data_list)):
        temp = data_list[i]
        j = i-1
        while j >= 0 and temp < data_list[j]:
            data_list[j+1] = data_list[j]
            j -= 1
            draw_on_screen(data_list, ["blue" if x == i or x == j or x == j+1 else "red" for x in range(len(data_list))])
            time.sleep(time_gap)
        data_list[j+1] = temp
    draw_on_screen(data_list, ["blue" for x in range(len(data_list))])


