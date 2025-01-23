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

#Use Raw string so that backslashes can be used in filepath

def read_weather_data(filepath: str):
    """
    Opens and reads file into a a list of tuples

    Args:
        The path to whatever weather_data file you'd like to read

    Returns:
        A list of tuples in the order of date (str), temperature (float), rainfall(float)
    """
    weather_data = []
    with open(filepath, 'r') as file:
        for line in file:
            date, temp, rainfall = line.split(",")
            weather_data.append((date, float(temp), float(rainfall)))
    return weather_data 

def calculate_average_temperature(weather_data):
    """
    Calculates the average temperature from the weather data.
    
    Args:
        weather_data (list): A list of tuples containing date, temperature, and rainfall data.
        
    Returns:
        float: The average temperature.
    """
    total_days = len(weather_data)
    total_temp = 0
    for i in weather_data:
        total_temp += i[1]
    avg_temp = total_temp/total_days
    return avg_temp

def calculate_total_rainfall(weather_data):
    """
    Calculates the total rainfall from the weather data.
    
    Args:
        weather_data (list): A list of tuples containing date, temperature, and rainfall data.
        
    Returns:
        float: The total rainfall.
    """
    total_rainfall = 0
    for i in weather_data:
        total_rainfall += i[2]
    return total_rainfall

def find_highest_temperature(weather_data):
    """
    Finds the highest temperature and its corresponding date.
    
    Args:
        weather_data (list): A list of tuples containing date, temperature, and rainfall data.
        
    Returns:
        tuple: A tuple containing the highest temperature (float) and the corresponding date (str).
    """
    highest_temp = None
    for i in weather_data:
        if highest_temp is None or i[1] > highest_temp:
            highest_temp = i[1]
            date = i[0]
    return float(highest_temp), str(date)

def find_lowest_temperature(weather_data):
    """
    Finds the lowest temperature and its corresponding date.
    
    Args:
        weather_data (list): A list of tuples containing date, temperature, and rainfall data.
        
    Returns:
        tuple: A tuple containing the lowest temperature (float) and the corresponding date (str).
    """
    lowest_temp = None
    for i in weather_data:
        if lowest_temp is None or i[1] < lowest_temp:
            lowest_temp = i[1]
            date = i[0]
    return float(lowest_temp), str(date)

def find_day_with_most_rainfall(weather_data):
    """
    Finds the day with the most rainfall and returns the date.
    
    Args:
        weather_data (list): A list of tuples containing date, temperature, and rainfall data.
        
    Returns:
        str: The date with the most rainfall.
    """
    most_rain = None
    for i in weather_data:
        if most_rain == None or i[2] > most_rain:
            date = i[0]
    return date


