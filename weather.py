import json
import tkinter as tk    
import requests
import time

def getWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=3296a18fee4693a179c720bab324d6b4"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] -21600  ))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] -21600  ))    
    
    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max. teplota: " + str(max_temp) + "\n" + "Min. teplota: " + str(min_temp) + "\n" + "Tlak: " + str(pressure) + "\n" + "Vlhkost vzduchu: " + str(humidity) + "\n" + "Rychlost vetra: " + str(wind) + "\n" + "Vychod slnka  : " + sunrise + "\n" + "Zapad slnka : " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Pocasie")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, justify='center', font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()

