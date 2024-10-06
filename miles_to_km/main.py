import tkinter as tk

window = tk.Tk()
window.title("Mile to Km converter")
window.minsize()
window.config(pady=20, padx=20)


def button_clicked():
    miles = float(inp.get())
    kilometers = miles * 1.609
    my_label.config(text=f"{kilometers}")


inp = tk.Entry(width=10, )
inp.grid(column=1, row=0)
inp.get()

button = tk.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

my_label = tk.Label(text="0", font=("arial", 24, "bold"))
my_label.grid(column=1, row=1)

lb1 = tk.Label(text="Is equal to:", font=("arial", 24, "bold"))
lb1.grid(column=0, row=1)
lb2 = tk.Label(text="Miles", font=("arial", 24, "bold"))
lb2.grid(column=2, row=0)
lb3 = tk.Label(text="Km", font=("arial", 24, "bold"))
lb3.grid(column=2, row=1)

window.mainloop()
