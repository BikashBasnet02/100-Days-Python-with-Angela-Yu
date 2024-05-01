# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it!")

# my_function()


# age = int(input("How old are you? "))
# if age > 18:
#     # print("You can vote at age", age)
#     print(f"You can vote at age {age}")



def mutate(a_list):
    b_list = []
    for new_item in a_list:
        new_item = new_item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 4, 5, 8, 13])   
