# Function to determine what clothing to wear given the current temperature.
def clothing_function(temperature):
    
    if sunny: 
        if temperature < 46:
            clothing = " heavy coat."
    if temperature > 46 and temperature < 69:
        clothing = " fleece jacket or big sweater and scarf."
    if temperature > 69:
        clothing = "optional light jacket."
   
    if cloudy:
        if temperature < 46:
            clothing = " heavy coat and scarf."
    if temperature > 46 and temperature < 69:
        clothing = " fleece jacket or big sweater and scarf."
    if temperature > 69:
        clothing = "light jacket."
    
    else:
        if sunny:
            if raining:
                if temperature < 46:
                    clothing = " heavy coat with umbrella."
    if temperature > 46 and temperature < 69:
        clothing = " rain jacket, sweater, and umbrella."
    if temperature > 69:
        clothing = "optional light jacket and umbrella."

    if cloudy:
        if raining:
            if temperature < 46:
                clothing = " heavy coat, scarf and umbrella."
    if temperature > 46 and temperature < 69:
        clothing = " fleece jacket or big sweater and scarf and don't forget the umbrella."
    if temperature > 69:
        clothing = "light jacket and umbrella."
    

    return clothing


#def main():
#    
#    testTemperature = 42
#
#    print(clothing_function(testTemperature))
#
#main()

