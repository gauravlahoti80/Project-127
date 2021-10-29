from tkinter import *
from tkinter.font import BOLD
import requests
from tkinter import messagebox

from requests import api


def fetchWeather():
    city = city_text.get()
    custom_link = 'http://api.openweathermap.org/data/2.5/weather?q=' + \
        city + '&units=metric&appid=22515dbe8047cf659da74a1cae281c2e'
    response = requests.get(custom_link)
    api_data = response.json()
    if api_data['cod'] == '404':
        messagebox.showerror('Error', 'City Not Found {}'.format(city))
    else:
        location['text'] = '{} , {}'.format(api_data['name'], api_data['sys']['country'])
        temperature['text'] = 'Temperature: {}°C'.format(api_data['main']['temp'])
        feels_like['text'] = 'Feels Like: {}'.format(api_data['main']['feels_like'])
        temp_min['text'] = 'Minimum Temperature: {}°C'.format(api_data['main']['temp_min'])
        temp_max['text'] = 'Maximum Temperature: {}°C'.format(api_data['main']['temp_max'])
        humidity['text'] = 'Humidity: {}'.format(api_data['main']['humidity'])

app = Tk()
app.title('Weather App')
app.geometry('700x350')
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_button = Button(app, text='Search', width=13, command=fetchWeather)
search_button.pack()

location = Label(app, text='', font=('bold', 20))
location.pack()

temperature = Label(app, text='', font=('bold', 20))
temperature.pack()

feels_like = Label(app, text='', font=('bold', 20))
feels_like.pack()

temp_min = Label(app, text='', font=('bold', 20))
temp_min.pack()

temp_max = Label(app, text='', font=('bold', 20))
temp_max.pack()

humidity = Label(app, text='', font=('bold', 20))
humidity.pack()

app.mainloop()
