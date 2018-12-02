def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]


text=input("Enter a String: ")

print ("The reverse string  is : " + reverse(text))
