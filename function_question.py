
def liters_100km_to_miles_gallon(liters_per_100km):
    miles_per_100km = 100000 / 1609.344  
    gallons = liters_per_100km / 3.785411784
    miles_per_gallon = miles_per_100km / gallons
    return miles_per_gallon

def miles_gallon_to_liters_100km(mpg):
    km_per_gallon = mpg * 1609.344 / 1000  
    liters_per_100km = 100 / (km_per_gallon / 3.785411784)
    return liters_per_100km


print(liters_100km_to_miles_gallon(5))


print(miles_gallon_to_liters_100km(47)) 