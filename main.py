import requests
from tkinter import *


def get_quote():
    # get(): get the end point
    response = requests.get(url="https://api.kanye.rest/")

    # HTTP status code
    # 1XX : hold on, 2XX: Success, 3XX: Go away, 4XX: (User)You screwed up, 5XX: (Servers)I screwed up
    response.raise_for_status()
    # get the data, use like the dictionary
    quotes = response.json()["quote"]
    canvas.itemconfig(quote_text, text=quotes, fill="black")


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 25, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()


