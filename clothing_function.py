# Function to determine what clothing to wear given the current temperature.
def clothing_function(temperature):
    
    if temperature < 46:
        clothing = " heavy coat."
    if temperature > 46 and temperature < 69:
        clothing = " fleece jacket or big sweater and scarf."
    if temperature > 69:
        clothing = "optional light jacket."
    
    return clothing


#def main():
#    
#    testTemperature = 42
#
#    print(clothing_function(testTemperature))
#
#main()

