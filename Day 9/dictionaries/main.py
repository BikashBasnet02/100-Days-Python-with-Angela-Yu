# Define a dictionary
# name is key and Alex is value
student = {
    "name": "Alex",    
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Science", "English"]
}

# Accessing dictionary elements
print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Student Grade:", student["grade"])
print("Subjects:", student["subjects"])

# Modifying dictionary
student["age"] = 21
student["grade"] = "B"
student["subjects"].append("History")

print("\nAfter Modification:")
print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Student Grade:", student["grade"])
print("Subjects:", student["subjects"])

# Adding new key-value pair
student["school"] = "XYZ High School"

print("\nAfter Adding School:")
print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Student Grade:", student["grade"])
print("Subjects:", student["subjects"])
print("School:", student["school"])

# Deleting key-value pair
del student["grade"]

print("\nAfter Deleting Grade:")
print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Subjects:", student["subjects"])
print("School:", student["school"])

# Iterating through dictionary
print("\nIterating through Dictionary:")
for key, value in student.items():
    print(key + ":", value) 

# nesting
    product_info = {
    "product_id": "12345",
    "name": "Laptop",
    "brand": "Dell",
    "price": 999.99,
    "stock": 50
}
    
#  Nesting a list in a Dictionary 
Travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}  

# Nesting Dictionary in a Dictionary
Travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

# Nesting Dictionary in a list
Travel_log = [
{
   "country":"France",
   "cities_visited":["Paris", "Lille", "Dijon"],
   "total_visits":12
},
{
   "country":"Germany",
   "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
   "total_visits":5
},
]