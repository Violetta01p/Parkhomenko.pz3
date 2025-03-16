number = float(input("Enter a floating pount number: "))
decimal_places = int(input("How many characters are needed after the comma? "))
formatted_number = f"{number:.{decimal_places}f}"
print(f"Formatted number: {formatted_number}")
