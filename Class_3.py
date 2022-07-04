# my_file = open("/Users/afik.navaro/Desktop/Class3text.txt", "r")  ### Loading the file in read state
# content = my_file.read() ### loading the content as read to value
# print(content)  ###printing the number of characters in content


# my_file = open("/Users/afik.navaro/Desktop/Class3text.txt", "a+") ### using a to append, + for read also
# content2 = my_file.write(" Navaro") ### writing to the file and putting what I wrote to content2 (will be number of indexes
# my_file.seek(0)   #### getting the cursor to the start of the file in order to read it
# content3 = my_file.read()    #### reading the file from index 0 (we used seek before to move the corsur to the start of the file
# print(content3)

# ### it is recommended to write the encoding (utf8, ACSII, etc) when openning a file, example:
# my_file = open("/Users/afik.navaro/Desktop/Class3text.txt", "r", encoding='UTF-8')
# print(my_file) ### will print file name with path, mode (last open command will override previous) and encoding
#
# my_file.close()  ### closing the file to allow usage by different user if neseccary, to save memory

# try:
#     my_file = open("/Users/afik.navaro/Desktop/Class3text.txt", "r")
#     my_file.write("aaa")
#     print(my_file)
# except IOError:
#     print("123")

    ### in order to save the error we can do the following
try:
    my_file = open("/Users/afik.navaro/Desktop/Class3text.txt", "r")
    my_file.write("aaa")
    print(my_file)
except IOError as e:   ### will save the error to e
    print("123")
    print(e)
finally:    ###the content under finally will be executed anyway, if try and except will fail both, it will run it and close the program
    print("always run")









