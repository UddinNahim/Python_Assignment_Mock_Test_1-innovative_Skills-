'''
Write a Python function categorize_temperature(temp) that takes the temperature in Celsius as input and returns "Cold" if the temperature is below 10, "Warm" if it is between 10 and 25, and "Hot" if it is above 25.
'''

def  categorize_temporature(temp):
    if temp < 10:
      return "Cold"
    elif temp >= 10 and temp <= 25:
      return "Warm"
    else:
      return "Hot"
print(categorize_temporature(10))
print(categorize_temporature(9))
print(categorize_temporature(20))
print(categorize_temporature(30))