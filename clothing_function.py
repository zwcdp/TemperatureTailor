

def main():
    clothing_function(42)


def clothing_function(temperature):
    clothing = ""
    
    if temperature < 46:
        clothing = "wear heave coat."
    if temperature > 46 and temperature < 69:
        clothing = "wear fleece jacket or big sweater and scarf."
    if temperature > 69:
        clothing = "optional light jacket."
    clothing = "enjoy the nice weather."
    
    print(clothing)
    return clothing