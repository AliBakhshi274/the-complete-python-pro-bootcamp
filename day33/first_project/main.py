import tkinter
import requests
import textwrap

text_on_image = None

def create_wrapped_text(canvas, x, y, width, text, font):
    global text_on_image
    lines = textwrap.wrap(text, width=width)
    y_coord = y
    for line in lines:
        text_on_image = canvas.create_text(x, y_coord, text=line, font=font, anchor=tkinter.NW)
        y_coord += 20

def load_data():
    global text_on_image
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    if hasattr(load_data, "text_items") and load_data.text_items:
        for item in load_data.text_items:
            canvas.delete(item)
    load_data.text_items = create_wrapped_text(canvas, 50, 50, 25, quote, ("Ariel", 12, "italic"))


window = tkinter.Tk()
window.title('API')
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(window, width=300, height=400)
load_image = tkinter.PhotoImage(file='photos/background.png')
canvas.create_image(150, 200, image=load_image)
canvas.grid(row=0, column=1, rowspan=2)

btn_image = tkinter.PhotoImage(file='photos/kanye.png')
btn = tkinter.Button(image=btn_image, command=load_data)
btn.grid(row=2, column=1)

load_data()


window.mainloop()