import tkinter

def action():
    miles = float(entry_miles.get())
    result = miles * 1.609344
    label_km_num.config(text=result)

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=400)
window.config(padx=100, pady=100)

entry_miles = tkinter.Entry(width=40)
entry_miles.grid(row=0, column=1)

label_miles = tkinter.Label(text="Miles")
label_miles.grid(row=0, column=2)

label_is_equal_to = tkinter.Label(text="Is equal to")
label_is_equal_to.grid(row=1, column=0)

label_km_num = tkinter.Label(text="0")
label_km_num.grid(row=1, column=1)

label_km = tkinter.Label(text="Km")
label_km.grid(row=1, column=2)

button = tkinter.Button(text="Calculate", command=action)
button.grid(row=2, column=1)














window.mainloop()