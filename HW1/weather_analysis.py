# Instructions:
# 1. **Remove the TODO comment and pass statement** once you’ve completed the function implementation.
#    - The TODO and pass are placeholders indicating that the function is not yet complete.
#    - Once the function is implemented, these should be removed to keep the code clean.
# 
# 2. **Best Coding Practices**:
#    - In professional programming, finalizing the code means removing unnecessary placeholders.
#    - This ensures your code is ready for review, testing, and does not contain clutter.
# 
# 3. **Adding Docstrings**:
#    - After removing TODO and pass, add a **docstring** for each function.
#    - The docstring should explain the function’s purpose, parameters, and expected output.
#    - Proper documentation improves code readability and helps with debugging and maintenance.

filepath = r"C:\Users\jchec\OneDrive\Documents\College\Sem2 24-25\CSE-2050\HW1\weather_data.txt" #Use Raw string so that backslashes can be used in filepath
def read_weather_data(filepath: str):
    weather_data = []
    with open(filepath, 'r') as file:
        for line in file:
            date, temp, rainfall = line.split(",")
            weather_data.append((date, float(temp), float(rainfall)))
    return(weather_data)
#Opens file and defines our list. reads file and strips excess whitespace, splits data by commas, appends data to list, returns the list

def calculate_average_temperature(weather_data):
    total_days = len(weather_data)
    total_temp = 0
    for data in weather_data:
        total_temp += data[1]
    avg_temp = total_temp/total_days
    return(avg_temp)


def calculate_total_rainfall(weather_data):
    """
    TODO: Calculates the total rainfall from the weather data.
    """
    pass

def find_highest_temperature(weather_data):
    """
    TODO: Finds the highest temperature and the corresponding date from the weather data.
    """
    pass


def find_lowest_temperature(weather_data):
    """
    TODO: Finds the lowest temperature and the corresponding date from the weather data.
    """
    pass

def find_day_with_most_rainfall(weather_data):
    """
    TODO: Finds the day with the most rainfall from the weather data.
    """
    pass

