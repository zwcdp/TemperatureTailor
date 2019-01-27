# Forms Alexa's reponse given the temperature and clothing.
def response_function(temperature, clothing):
    return "Based on the weather, you should wear " + clothing + " because the temperature is " + str(temperature) + " degrees."

# For testing only.
def main():
    print(response_function(56.3, "raincoat"))

main()
