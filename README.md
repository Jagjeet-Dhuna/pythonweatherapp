# PythonWeatherApp

pythonweatherapp is a simple Python application that provides real-time weather information based on the user's city input. It utilizes the OpenWeatherMap API to fetch weather data such as weather description and temperature and then displays it in a user-friendly GUI built with Tkinter.

![A gif of the weather app in use](https://github.com/Jagjeet-Dhuna/pythonweatherapp/assets/48265165/e1a8ac91-692a-47d6-bb56-dcefbf959ca8)


## Features

- Real-time weather updates. (to be automated for live updates)
- Temperature display in Celsius or Fahrenheit.
- Simple and intuitive GUI.
- Customizable city input.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Requests library
- Tkinter (usually pre-installed with Python)

### Installing

A step-by-step series of examples that tell you how to get a development environment running:

Clone the repository:

```bash
git https://github.com/Jagjeet-Dhuna/pythonpythonweatherapp.git
```
Navigate to the cloned directory:

```bash
cd pythonweatherapp
```
Install the required packages:

```bash
pip install requests
```

### API Key
The application requires an API key from OpenWeatherMap.

Insert your API key in the config.py file:

```python
api_key = 'YOUR_API_KEY'
```

### Running the Application
To run the application, simply execute the pythonweatherapp.py script:
