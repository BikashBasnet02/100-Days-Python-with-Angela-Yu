print('Namaste! Welcome to the Band Name Generator.')

# Prompt the user for their city and pet's name
city = input('Which city did you grow up in? ')
pet_name = input('Tell me the name of a pet: ')

# Generate the band name
band_name = city.capitalize() + ' ' + pet_name.capitalize()

# Display the band name to the user
print('Your band name could be:', band_name)
