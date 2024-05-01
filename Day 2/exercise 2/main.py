# -------BMI calculator
height = input('Enter your height in m: ')
weight = input('Enter your weight in kg: ')

BMI = int(weight) / float(height) ** 2
BMI_as_int = int(BMI)
print(BMI_as_int)