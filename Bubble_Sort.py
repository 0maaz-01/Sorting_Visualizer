import time

def bubble_sort(data_list, draw_on_screen, time_gap):
    for r in range(1, len(data_list)):
        for i in range(len(data_list)-r):
            if data_list[i] > data_list[i+1]:
                data_list[i],data_list[i+1] = data_list[i+1], data_list[i]
                draw_on_screen(data_list, ["blue" if x == i or x == i+1 else "red" for x in range(len(data_list))])
                time.sleep(time_gap)
    draw_on_screen(data_list, ["blue" for x in range(len(data_list))])

