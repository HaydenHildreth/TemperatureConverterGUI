import tkinter as tk


def f2c(t):
    global label_output
    temp = int(t)
    temp_f = round((temp - 32) * 5 / 9, 2)
    label_output.configure(text=f'Your number is: {temp_f}')


def c2f(t):
    global label_output
    temp = int(t)
    temp_f = round((temp * (9 / 5)) + 32, 2)
    label_output.configure(text=f'Your number is: {temp_f}')


def logic():
    for i in lb_listbox.curselection():
        choice = lb_listbox.get(i)
    temp = entry_input.get()
    if choice == 'F2C':
        f2c(temp)
    elif choice == 'C2F':
        c2f(temp)
    else:
        raise Exception('ERROR')


root = tk.Tk()
root.title("Temperature Converter GUI")

label_input = tk.Label(root, text='Please input your temperature: ')
label_input.grid(row=0, column=0)
entry_input = tk.Entry(root)
entry_input.grid(row=0, column=1)

options = ['F2C', 'C2F']
label_listbox = tk.Label(root, text='Choose your function: ')
label_listbox.grid(row=1, column=0)
lb_listbox = tk.Listbox(root)
lb_listbox.grid(row=1, column=1)
lb_listbox.config(height=2)
for option in options:
    lb_listbox.insert(tk.END, option)

label_output = tk.Label(root, text='Your number is: ')
label_output.grid(row=2, column=0)

button = tk.Button(root, text='Convert!', command=logic)
button.grid(row=3)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
