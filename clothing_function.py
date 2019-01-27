# Function to determine what clothing to wear given the current temperature.
def clothing_function(temperature, raining, clear):
    
    if clear: 
        if temperature < 46:
            if raining:
                clothing = " a heavy coat with umbrella."
            else:
                clothing = " a heavy coat."
        if temperature > 46 and temperature < 69:
            if raining:
                clothing = " a rain jacket, sweater, and umbrella."
            else:
                clothing = " a fleece jacket, or a big sweater and scarf."
        if temperature > 69:
            if raining:
                clothing = " an umbrella and optional light jacket"
            else:
                clothing = " an optional light jacket."
    else:
        if temperature < 46:
            if raining:
                clothing = " a heavy coat, scarf, and umbrella"
            else:
                clothing = " a heavy coat and scarf."
        if temperature > 46 and temperature < 69:
            if raining:
                clothing = " a fleece jacket, or a big sweater and scarf. Also, don't forget your umbrella."
            else:
                clothing = " a fleece jacket, or a big sweater and scarf."
        if temperature > 69:
            if raining:
                clothing = " a light jacket and umbrella."
            else:
                clothing = " a light jacket."

    return clothing


#def main():
#   
#    testTemperature = 68
#    testRaining = False
#    testClear = True
#
#    print(clothing_function(testTemperature, testRaining, testClear))
#
#main()

