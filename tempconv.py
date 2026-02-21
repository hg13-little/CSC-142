import pygame
import pygwidgets
import sys

pygame.init()

# Window setup
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Temperature Converter')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Text input for temperature
tempInput = pygwidgets.InputText(
    window,
    (50, 50),
    '',
    fontSize=24,
    width=200
)

# Radio buttons
toFahrenheit = pygwidgets.TextRadioButton(
    window,
    (50, 120),
    'toF',
    'Convert to Fahrenheit',
    1
)

toCelsius = pygwidgets.TextRadioButton(
    window,
    (50, 160),
    'toC',
    'Convert to Celsius',
    1
)

# Set default selection
toFahrenheit.setValue(True)
toCelsius.setValue(False)

# Convert button
convertButton = pygwidgets.TextButton(
    window,
    (50, 220),
    'Convert'
)

# Output display
outputText = pygwidgets.DisplayText(
    window,
    (50, 300),
    'Result will appear here',
    fontSize=24,
    textColor=BLACK
)


# Conversion function
def doConversion():
    text = tempInput.getValue()

    try:
        temp = float(text)

        if toFahrenheit.getValue():
            result = temp * 9/5 + 32
            outputText.setValue(str(round(result, 2)) + " °F")
        else:
            result = (temp - 32) / (9/5)
            outputText.setValue(str(round(result, 2)) + " °C")

    except:
        outputText.setValue("Invalid input")


# Main loop
while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Enter key in input
        if tempInput.handleEvent(event):
            doConversion()

        # Radio buttons
        toFahrenheit.handleEvent(event)
        toCelsius.handleEvent(event)

        # Convert button
        if convertButton.handleEvent(event):
            doConversion()

    # Draw everything
    window.fill(WHITE)

    tempInput.draw()
    toFahrenheit.draw()
    toCelsius.draw()
    convertButton.draw()
    outputText.draw()

    pygame.display.update()
    


