file_binario = None

with open("yamahaR1.jpg","rb") as file:

    file_binario = file.read()
    print(file_binario)

with open("file_binario.jpg","wb") as file:

    file.write(file_binario)
    

