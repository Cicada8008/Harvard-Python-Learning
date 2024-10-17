def convert(input_text):
    converted_text = input_text.replace(':)', '🙂').replace(':(', '🙁')
    return converted_text

def main():
    user_input = input("Enter some text: ")
    result = convert(user_input)
    print(result)


main()



