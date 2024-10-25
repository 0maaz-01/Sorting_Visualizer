from customtkinter import *
import random
from Bubble_Sort import bubble_sort
from Quick_Sort import quick_sort
from Merge_Sort import merge_sort
from Selection_Sort import selection_sort
from Insertion_Sort import insertion_sort

brown = "#322D29"
red = "#72383D"
light_brown = "#AC9C8D"
dark_white = "#D1C7BD"
my_font = ("Castellar",20,"bold")
button_color = "#A48374"

data = []

def start():
    global data
    if not data:
        return
    if algorithm_box.get().lower() == "quick sort":
        quick_sort(data, 0, len(data)-1, draw_on_screen, speed_slider.get()/100)
        draw_on_screen(data, ['green' for x in range(len(data))])
    elif algorithm_box.get().lower() == "bubble sort":
        bubble_sort(data, draw_on_screen, speed_slider.get()/100)
    elif algorithm_box.get().lower() == "merge sort":
        merge_sort(data, draw_on_screen, speed_slider.get() / 100)
        draw_on_screen(data, ['green' for x in range(len(data))])
    elif algorithm_box.get().lower() == "selection sort":
        selection_sort(data, draw_on_screen, speed_slider.get()/100)
    elif algorithm_box.get().lower() == "insertion sort":
        insertion_sort(data, draw_on_screen, speed_slider.get()/100)


def draw_on_screen(data, colors):
    canvas.delete("all")
    canvas_width = window.winfo_width() - 30
    canvas_height =  2 * window.winfo_height()//3
    x_width = canvas_width / (len(data) + 1)
    offset = 10
    spacing_bet_rect = 10
    normalised_data = [i/max(data) for i in data]

    for i, height in enumerate(normalised_data):
        x0 = (i * x_width) + offset + spacing_bet_rect
        y0 = canvas_height - height * 400

        x1 = (i+1) * x_width
        y1 = canvas_height

        canvas.create_rectangle(x0,y0,x1,y1, fill = colors[i])
        canvas.create_text(x0+2, y0, anchor = SW, text = str(data[i]), font = ("Castellar",20,"bold"), fill = "orange")
    window.update_idletasks()

def generate():
    global data
    canvas.delete("all")

    mini_value = int(min_val_slider.get())
    maxi_value = int(max_val_slider.get())
    size = int(size_slider.get())

    if maxi_value < mini_value:
        maxi_value, mini_value = mini_value, maxi_value

    data = []
    for _ in range(size):
        data.append(random.randrange(mini_value, maxi_value+1))

    draw_on_screen(data, ["red" for x in range(len(data))])

def display_speed(value):
    speed_value.configure(text = int(value))

def display_size(value):
    size_value.configure(text = int(value))

def display_min(value):
    min_value.configure(text = int(value))
def display_max(value):
    max_value.configure(text = int(value))


window = CTk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = int(screen_width * 0.7)
window_height = int(screen_height * 0.7)
starting_x = screen_width//6
starting_y = screen_height//6
window.config(background=dark_white)
window.geometry(f"{window_width}x{window_height}+{starting_x}+{starting_y}")
window.resizable(False, False)

canvas = CTkCanvas(window, width = window.winfo_width() -30, height = 2*window.winfo_height()//3, background="black")
canvas.place(relx = 0.01, rely = 0.01)

#############################################################    Button Frame     ########################################################################
button_frame = CTkFrame(window, fg_color=dark_white, width=window_width+5, border_width=0, corner_radius=0)
button_frame.place(relx = 0, rely = 0.7)

# Algorithm
algorithm_label = CTkLabel(master = button_frame, corner_radius=0, text = "Algorithm:", fg_color=dark_white, text_color="black", font=my_font)
algorithm_label.place(relx = 0.01, rely = 0.01)

algorithm_box =  CTkComboBox(master=button_frame, corner_radius = 0, font = my_font, dropdown_font=my_font, dropdown_fg_color="#3A2D28",fg_color="#3A2D28",width = window_width//4,values=["Bubble Sort", "Quick Sort", "Merge Sort", "Insertion Sort", "Selection Sort"])
algorithm_box.set("Select Algorithm")
algorithm_box.place(relx = 0.17, rely = 0)

# Speed
speed_label = CTkLabel(master = button_frame, corner_radius=0, text = "Speed:", fg_color=dark_white, text_color="black", font=my_font)
speed_label.place(relx = 0.65, rely = 0.01)

speed_slider = CTkSlider(master=button_frame, from_= 0, to=50, number_of_steps=100, command=display_speed, progress_color="teal")
speed_slider.place(relx = 0.73, rely = 0.03)

speed_value = CTkLabel(master=button_frame , font=my_font, text_color="black", text="")
speed_value.place(relx = 0.81 , rely = 0.11)

# Size
size_label = CTkLabel(master = button_frame, corner_radius=0, text = "Size:", fg_color=dark_white, text_color="black", font=my_font)
size_label.place(relx = 0.01, rely = 0.3)

size_slider = CTkSlider(master=button_frame, from_=3, to=39, number_of_steps=100, command=display_size, progress_color="teal")
size_slider.place(relx = 0.07, rely = 0.32)

size_value = CTkLabel(master=button_frame , font=my_font, text_color="black", text="")
size_value.place(relx = 0.15 , rely = 0.4)


# Min Value
min_val_label = CTkLabel(master = button_frame, corner_radius=0, text = "Min Value:", fg_color=dark_white, text_color="black", font=my_font)
min_val_label.place(relx = 0.28, rely = 0.3)

min_val_slider = CTkSlider(master=button_frame, from_=0, to=100, number_of_steps=100, command = display_min,progress_color="teal")
min_val_slider.place(relx = 0.43, rely = 0.32)

min_value = CTkLabel(master=button_frame , font=my_font, text_color="black", text="")
min_value.place(relx = 0.51 , rely = 0.4)


# Max Value
max_val_label = CTkLabel(master = button_frame, corner_radius=0, text = "Max Value:", fg_color=dark_white, text_color="black", font=my_font)
max_val_label.place(relx = 0.64, rely = 0.3)

max_val_slider = CTkSlider(master=button_frame, from_=0, to=100, number_of_steps=100, command=display_max, progress_color="teal")
max_val_slider.place(relx = 0.79, rely = 0.32)

max_value = CTkLabel(master=button_frame , font=my_font, text_color="black", text="")
max_value.place(relx = 0.87 , rely = 0.4)


# Start Button
start_btn = CTkButton(master = button_frame, text = "Start", corner_radius = 0,  font = ("Castellar",30,"bold"), command = start,hover_color = "#A48374", fg_color = "#3A2D28" )#, border_width=2,border_color="#FFCC70")# fg_color = "transparent")
start_btn.place(relx = 0.35, rely = 0.65, anchor = "center")

# Generate Button
generate_btn = CTkButton(master = button_frame, text = "Generate", corner_radius = 0, command = generate ,font =  ("Castellar",30,"bold") ,hover_color = "#A48374", fg_color = "#3A2D28" )#, border_width=2,border_color="#FFCC70")# fg_color = "transparent")
generate_btn.place(relx = 0.6, rely = 0.65, anchor = "center")

###########################################################    Button Frame Ends Here    #########################################################################

window.mainloop()