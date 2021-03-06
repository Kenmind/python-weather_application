#!/usr/bin/python3
"""Python weather application"""
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

app = Tk()
app.title("WEATHER APPLICATION")
app.geometry("900x500+300+200")
app.resizable(False, False)

def getWeather():
    """ Get current weather updates"""
    try:
        city = textfield.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER UPDATE FOR THIS CITY")

        #OpenWeatherMapAPI Request
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=26d7ea49a3374452ae2e7e867d04c597"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!!!")

""" Search Box """
Search_image = PhotoImage(file="images/search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(app, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border="1", fg="beige")

textfield.place(x=50, y=40)
textfield.focus()

search_icon = PhotoImage(file="images/search_icon.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="green", command=getWeather)
myimage_icon.place(x=399, y=31)

#logo
logo_image = PhotoImage(file="images/logo.png")
logo = Label(image=logo_image)
logo.place(x=150, y=140)

logo_image1 = PhotoImage(file="images/logo2.png")
logo1 = Label(image=logo_image1)
logo1.place(x=500, y=1)


#Bottom Box
Frame_image = PhotoImage(file="images/box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

#time
name = Label(app, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(app, font=("Helvetica",20))
clock.place(x=30, y=130)

#Labels
label0 = Label(app, text="WIND SPEED", font=("Helvetica", 15, "bold"), fg="white", bg="#1AB5EF")
label0.place(x=110,y=400)

label1 = Label(app, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1AB5EF")
label1.place(x=260,y=400)

label2 = Label(app, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1AB5EF")
label2.place(x=430,y=400)

label3 = Label(app, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1AB5EF")
label3.place(x=650,y=400)

t = Label(font=("arial", 70, "bold"), fg="#EE666D")
t.place(x=400, y=250)

c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=230)

company_name = Label(app, text="The_Masterminds", font=("times", 10, "bold", "italic"), fg="#404040")
company_name.place(x=30, y=1)

developer_name = Label(app, text="Kennedy Kalaluka", font=("times", 8, "bold", "italic"), fg="#404040")
developer_name.place(x=58, y=13)

tutor_name = Label(app, text="Copyright of Parvat Computer Technology (youtube channel)", font=("times", 8, "bold", "italic"), fg="black")
tutor_name.place(x=300, y=480)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1AB5EF")
w.place(x=120, y=430)

h = Label(text="...", font=("arial", 20, "bold"), bg="#1AB5EF")
h.place(x=280, y=430)

d = Label(text="...", font=("arial", 20, "bold"), bg="#1AB5EF")
d.place(x=430, y=430)

p = Label(text="...", font=("arial", 20, "bold"), bg="#1AB5EF")
p.place(x=670, y=430)

app.mainloop()
