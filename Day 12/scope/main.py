# -----scope

person = 1
def increase_person_number():
    person = 2
    print(f'Person inside function: {person}')

increase_person_number()
print(f'person outside funtion: {person}')



# Local scope

def drink_potion():
    potion_strength =2
    print(potion_strength)

# drink_potion()
# print(potion_strength)


# Global scope 

player_health = 100
potion_strength = 2
print(potion_strength)

drink_potion()

# Global constants 
PI =3.14159
URL = "http://www.google.com"



