from tkinter import *
import calendar

def calendar_see():
    window = Tk()
    window.config(background="light pink")
    window.title("Complete calendar")
    window.geometry("900x600")  # Adjusted to a larger size for better display
    get_yr = int(year_entry.get())
    window_content = calendar.calendar(get_yr)
    yr_cal = Text(window, font=("Arial", 10, "bold"), wrap=NONE)
    yr_cal.insert(END, window_content)
    yr_cal.config(state=DISABLED)
    yr_cal.grid(row=0, column=0, padx=10, pady=10)

    # Add scrollbars for better navigation
    scrollbar_y = Scrollbar(window, orient=VERTICAL, command=yr_cal.yview)
    scrollbar_y.grid(row=0, column=1, sticky='ns')
    yr_cal.config(yscrollcommand=scrollbar_y.set)

    scrollbar_x = Scrollbar(window, orient=HORIZONTAL, command=yr_cal.xview)
    scrollbar_x.grid(row=1, column=0, sticky='ew')
    yr_cal.config(xscrollcommand=scrollbar_x.set)

    window.mainloop()

if __name__ == '__main__':
    root = Tk()
    root.config(background="yellow")
    root.title("GUI Calendar")
    root.geometry("590x340")
    name = Label(root, text="Calendar", bg="blue", font=("Arial", 35, "bold"))
    name.grid(row=0, column=0, padx=10, pady=10)
    year = Label(root, text="Enter a year", bg="light pink", font=("Arial", 35, "bold"))
    year.grid(row=1, column=0, padx=10, pady=10)
    year_entry = Entry(root, font=("Arial", 35, "bold"))
    year_entry.grid(row=2, column=0, padx=10, pady=10)
    show_button = Button(root, text="Show Calendar", fg="red", bg="black", font=("Arial", 35, "bold"), command=calendar_see)
    show_button.grid(row=3, column=0, padx=10, pady=10)
    root.mainloop()
