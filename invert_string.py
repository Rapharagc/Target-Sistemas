user_string = input("Digite uma palavra: ")


def reverse_string(s):
    reversed_string = ""
    for character in s:
        reversed_string = character + reversed_string  
    return reversed_string



print("A forma invertida da palavra é:", reverse_string(user_string))