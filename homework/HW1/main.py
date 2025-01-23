import weather_analysis as wa

filepath = r"C:\Users\jchec\OneDrive\Documents\College\Sem2 24-25\CSE-2050\homework\HW1\weather_data.txt"
def weather_analyze(filepath):
    """
    Uses all functions from weather_analysis.py to analyze weather

    Args:
    The path to whatever weather_data you'd like to have analyzed

    Returns:
    A dictionary of different weather statistics (avg temp, highest temp, lowest temp, most rainfall)
    """
    data = wa.read_weather_data(filepath)
    results = {"Avg Temp": wa.calculate_average_temperature(data),
           "Total Rainfall": wa.calculate_total_rainfall(data),
           "Highest Temp": wa.find_highest_temperature(data),
           "Lowest Temp": wa.find_lowest_temperature(data),
           "Most Rainfall":wa.find_day_with_most_rainfall(data)
    }
    return results

if __name__ == "__main__":
    
    results = weather_analyze(filepath) #or the path to the file
    print(results)