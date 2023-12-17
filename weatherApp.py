import requests
import tkinter as tk
import config

# Constants
api_key = config.api_key
url = 'http://api.openweathermap.org/data/2.5/weather?'

# Conversion function
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Weather update function
def update_weather():
    city = cityinput.get()
    complete_url = url + 'appid=' + api_key + '&q=' + city + '&units=metric'
    response = requests.get(complete_url)
    data = response.json()

    if data.get('cod') == 200:
        main_data = data['main']
        temperature = main_data['temp']
        temp_min = main_data['temp_min']
        temp_max = main_data['temp_max']
        weather_description = data['weather'][0]['description']

        unit = selected_temp_unit.get()
        if unit == 'fahrenheit':
            temperature = celsius_to_fahrenheit(temperature)
            temp_min = celsius_to_fahrenheit(temp_min)
            temp_max = celsius_to_fahrenheit(temp_max)
            temp_unit = 'F'
        else:
            temp_unit = 'C'
        
        actualtemp.config(text=f'{temperature:.0f}°{temp_unit}')
        Hightemp.config(text=f'{temp_max:.0f}°{temp_unit}')
        Lowtemp.config(text=f'{temp_min:.0f}°{temp_unit}')
        conditions.config(text=weather_description.capitalize())
    else:
        actualtemp.config(text='NA')
        conditions.config(text='Error or City not found')
        Hightemp.config(text='NA')
        Lowtemp.config(text='NA')

# Initialize Tkinter window
root = tk.Tk()
root.title('Weather Forecast')
root.iconbitmap('sun.ico')
root.geometry('640x280')
root.resizable(False, False)
root.configure(background='gray4')

# Configure grid layout
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=0)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

# City Entry
cityinput = tk.Entry(root, background='gray12', foreground='white', borderwidth=0, selectborderwidth=0, relief='flat', font=('Courier', 18))
cityinput.grid(row=0, column=0, columnspan=4, padx=(10, 0), pady=10, sticky='ew')

# Search Button
button = tk.Button(root, text='Search', background='grey20', foreground='white', relief='flat', command=update_weather)
button.grid(row=0, column=4, padx=(0, 10), pady=10, sticky='ns') 

# Radio button variable
selected_temp_unit = tk.StringVar(value='celsius')

# Styling for the radio buttons
radio_style = {'background': 'gray4', 'foreground': 'white', 'selectcolor': 'gray20', 'activebackground': 'gray4', 'activeforeground': 'white', 'font': ('Courier', 16), 'relief': 'flat'}

# Celsius and Fahrenheit Radio Buttons
cradio = tk.Radiobutton(root, text='Celsius', variable=selected_temp_unit, value='celsius', command=update_weather, **radio_style)
fradio = tk.Radiobutton(root, text='Fahrenheit', variable=selected_temp_unit, value='fahrenheit', command=update_weather, **radio_style)
cradio.grid(row=3, column=1, padx=(0, 10), pady=10, sticky='ns') 
fradio.grid(row=3, column=2, padx=(0, 10), pady=10, sticky='ns') 

# Labels for temperature and conditions
temptitle = tk.Label(root, text='Actual Temp', foreground='white', background='gray4', font=('Courier', 16))
actualtemp = tk.Label(root, text='0', foreground='white', background='gray4', font=('Courier', 64))
conditions = tk.Label(root, text='Clear', foreground='white', background='gray4', font=('Courier', 16))
hightitle = tk.Label(root, text='High', foreground='white', background='gray4', font=('Courier', 16))
Hightemp = tk.Label(root, text='0', foreground='white', background='gray4', font=('Courier', 32))
lowtitle = tk.Label(root, text='Low', foreground='white', background='gray4', font=('Courier', 16))
Lowtemp = tk.Label(root, text='0', foreground='white', background='gray4', font=('Courier', 32))

# Positioning the labels
temptitle.grid(row=1, column=0, padx=10, pady=10, sticky='w')
actualtemp.grid(row=2, column=0, padx=10, pady=10, sticky='w')
conditions.grid(row=3, column=0, padx=10, pady=10, sticky='w')
hightitle.grid(row=1, column=1, padx=10, pady=10, sticky='w')
Hightemp.grid(row=2, column=1, padx=10, pady=10, sticky='w')
lowtitle.grid(row=1, column=2, padx=10, pady=10, sticky='w')
Lowtemp.grid(row=2, column=2, padx=10, pady=10, sticky='w')

root.mainloop()
