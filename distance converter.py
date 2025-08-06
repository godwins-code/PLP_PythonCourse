print("Distance Converter".title())

first_name = input("Name: ").upper()
distance_in_km = float(input("Distance(km): "))
distance_in_miles = float(round(distance_in_km * 1.609))

print(f'Hello {first_name}.', f'Distance(km): {distance_in_km}.',
      f'Distance(mile): {distance_in_miles}', sep='\n')
