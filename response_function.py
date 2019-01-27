def whatsthe_weather( temperature, clothing ):
    alexa_reply = "Based on the weather, you should wear " + clothing + " because the temperature is " + temperature

    return alexa_reply


result = whatsthe_weather("50", "str")
print(result)
