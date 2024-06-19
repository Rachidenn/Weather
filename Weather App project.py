import tkinter as tk
from tkinter import *
import requests
from tkinter import messagebox as mb

# Function to get weather notification
def getWeatherNotification():
    cityName = place.get()  # Get the city name from the entry widget
    api_key = '6dcc75083708e126a5da8c82c12f2ae5'  # Replace with your API key
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"

    try:
        # Complete URL for fetching weather data
        url = f"{baseUrl}q={cityName}&appid={api_key}"

        # Sending HTTP request
        response = requests.get(url)

        # Checking if the response is successful
        if response.status_code == 200:
            # Converting response content to JSON format
            data = response.json()

            # Extracting weather information
            main = data['main']
            temperature = main['temp'] - 273.15  # Convert from Kelvin to Celsius
            pressure = main['pressure']
            humidity = main['humidity']

            # Extracting weather description
            weather = data['weather']
            weather_desc = weather[0]['description']

            # Constructing the notification message
            info = f"Weather in {cityName}:\nTemperature: {temperature:.1f}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nDescription: {weather_desc}"

            # Displaying notification using messagebox
            mb.showinfo("Weather Notification", info)

        else:
            mb.showerror('Error', f"Error fetching data: Status Code {response.status_code}")

    except Exception as e:
        mb.showerror('Error', str(e))

# Create the main window
wn = Tk()
wn.title("PythonGeeks Weather Alert")
wn.geometry('700x200')
wn.config(bg='azure')

# Heading label
Label(wn, text="PythonGeeks Weather Desktop Notifier", font=('Courier', 15), fg='grey19', bg='azure').place(x=100, y=15)

# Label and Entry for getting the city name
Label(wn, text='Enter the Location:', font=("Courier", 13), bg='azure').place(relx=0.05, rely=0.3)
place = Entry(wn, width=50)
place.place(relx=0.5, rely=0.3)

# Button to get weather notification
btn_get_notification = Button(wn, text='Get Notification', font=7, fg='grey19', command=getWeatherNotification)
btn_get_notification.place(relx=0.4, rely=0.75)

# Start the main event loop
wn.mainloop()
