try:
    file = open('test.txt')
    a_dictionary = {"key": "value"}
    print(a_dictionary['key'])
except FileNotFoundError:
    print("File not found")
    file = open('test.txt', 'w')
    file.write("Something")
except KeyError as error_message:
    print(f"Key Error: {error_message}")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File closed")