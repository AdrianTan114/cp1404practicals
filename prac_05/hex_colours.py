"""Hex codes to colours in a dictionary."""

NAME_TO_HEX = {"Scarlet": "#ff2400", "Sapphire": "#0f52ba", "Mustard": "#ffdb58", "Vermillion": "#e34234",
               "Rose": "#ff007f", "Viridian": "#40826d", "Burgundy": "#800020", "Khaki": "#f0e68c",
               "Lavender": "#e6e6fa", "Olive": "#808000", "Plum": "#8e4585", "Silver": "#c0c0c0", "Zomp": "#39a78e"}

colour = input("Enter a colour name: ").title()
while colour != "":
    try:
        print(f"{colour} is {NAME_TO_HEX[colour]}")
    except KeyError:
        print("Colour name not in dictionary.")
    colour = input("Enter a colour name: ").title()
print("Finish")
