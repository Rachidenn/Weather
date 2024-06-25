import tkinter as tk
from tkinter import *
import requests
from tkinter import messagebox as mb

def getWeatherNotification():
    cityName = place.get()  # Get the city name from the entry widget
    api_key = '6dcc75083708e126a5da8c82c12f2ae5'  
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"

    try:
       
        url = f"{baseUrl}q={cityName}&appid={api_key}"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            main = data['main']
            temperature = main['temp'] - 273.15  
            pressure = main['pressure']
            humidity = main['humidity']

            weather = data['weather']
            weather_desc = weather[0]['description']

            info = f"Weather in {cityName}:\nTemperature: {temperature:.1f}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nDescription: {weather_desc}"

            mb.showinfo("Weather Notification", info)

        else:
            mb.showerror('Error', f"Error fetching data: Status Code {response.status_code}")

    except Exception as e:
        mb.showerror('Error', str(e))

wn = Tk()
wn.title("PythonGeeks Weather Alert")
wn.geometry('700x200')
wn.config(bg='azure')

Label(wn, text="PythonGeeks Weather Desktop Notifier", font=('Courier', 15), fg='grey19', bg='azure').place(x=100, y=15)

Label(wn, text='Enter the Location:', font=("Courier", 13), bg='azure').place(relx=0.05, rely=0.3)
place = Entry(wn, width=50)
place.place(relx=0.5, rely=0.3)

btn_get_notification = Button(wn, text='Get Notification', font=7, fg='grey19', command=getWeatherNotification)
btn_get_notification.place(relx=0.4, rely=0.75)

wn.mainloop()
