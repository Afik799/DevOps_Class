# #1 + 2
#
# try:
#     a = 1 / 0
# except ZeroDivisionError:
#     print("Division by zero is not accepted.")
#
# #3 the code will work and legal, as finally will be printed, if x = 1 raises and exception finally will still print
# #anyhow, try condition is working, so no code break, and finally will still be printed.
#
# try:
#     x = 1
# finally:
#     print("finally")
#
# #4 except can catch in error followed by the word Error for example IOError
#
# #5 the code will be printed, even if there is error
#
# #6
# # except IOError will catch basically any input/output operation which is failing
# # except ZeroDivisionError will catch division by zero to avoid crash by from division by zero
# #7
#
# wordsfile = open("/Users/afik.navaro/words.txt", "a+")
#
# #8
#
# # wordsfile.write("Afik Navaro")
#
# #9
#
# wordsfile.seek(0)
# print(wordsfile.read())
#
# #10
#
# wordsfile.write("תוכן בעברית")
# wordsfile.seek(0)
# print(wordsfile.read())

# 11
# import flask
# from flask import Flask
#
# pwd = input("Enter pwd of file: ")
#
# app = Flask(__name__)


# @app.route("/content")
# def get_txt():
#     content = open(f"{pwd}", "r")
#     if ".txt" in pwd:
#         return content.read(), 200
#     else:
#         return "not a text file", 404
#
#
# @app.route("/register")
# def hello():
#     content = open(f"{pwd}", "w+")
#     if ".txt" in pwd:
#         content.write("Hello")
#         return "success", 201
#     else:
#         return "not a text file", 404
#
#
# app.run(host='localhost', debug=True, port=5000)


# from PIL import Image
#
# img = Image.new('RGB', (100, 100), color='red')
# img.save('pil_red.png')