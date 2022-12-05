countries_capitals = {"Nepal":"Kathmandu", "India":"New Delhi", "Afghanistan":"Kabul", "Pakistan":"Islamabad", "Spain":"Madrid", "France":"Paris", "England":"London"}

while True:
    country = input("Enter a country (or Type quit to exit): ")
    country = country.capitalize()

    if country == "Quit":
        break
    elif country in countries_capitals:
        print(f"{country}'s capital city is {countries_capitals[country]}.")
    else:
        capital = input(f"No data available.\nPlease enter {country}'s capital: ")
        capital = capital.capitalize()
        countries_capitals[country] = capital