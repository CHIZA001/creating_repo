# """
# string manupulation
# """
# school= "modibbo adama university yola"
# school2 = "american university of nigeria"
# text = """
# welcome to mentors innncation hub nigeria we are glad you re here with us today.
# your presence is most value and we will give you the best ant client can offer.
# """
# greeting = "how are you!"
# question = "what would you have for you today?"
# #count
# print("character count:",len(school))
# print("data type:",type(school2))
# print("character count:",len(school2))
# #slicing
# print(school[8:12])
# # full_name= first_name + "," + last_name
# # fullname="samuel, gregory"
# # print(f' hello! {full_name},{last_name}')
# firstname="Samuel"
# lastname="Gregory"
# full_name = firstname + " " + lastname
# print(f'hello! {firstname}, {lastname}')
# slicedinit=full_name[7]
# print(f"{slicedinit}.{firstname}")
# repeat="Hi!"*10
# print(repeat)
# item="playstation 5"
# price=600000
# receipt = f"You bought a {item}\nTotal:\tN{price}"
# print(receipt)
# text="python is fun"
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())
# print(text.swapcase())
# # Lesson 5: search and check methods
# sentence="hello, welcome to python class."
# print(sentence.find("python"))
# print(sentence.startswith("welcome"))
# print(sentence.endswith("class."))
# print("1234".isdigit)
# print("check full name", full_name.endswith("he"))
# print("check full name", full_name.startswith("gregory"))
# # Lesson 6: split and join methods
# words = sentence.split()
# print(words)
# joined=" ".join(words)
# print(joined)
# #Lesson 7: strip methods and clean text
# dirty_text = "   Hello, World!   "
# cleaned_text = dirty_text.strip()
# a = 33
# b =22
# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print("a and b are equal")
# else :
#     print("a is greater than b")