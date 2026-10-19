
def main():
    message = input("type in message: ")
    emoji_message = convert(message)
    print(emoji_message)

def convert(message):
    #emoji_message = message.replace(":)", "opfer")
    #print(emoji_message)
    
    emoji_message = message.replace(":(", "🙁")
    emoji_message = emoji_message.replace(":)", "🙂")
    return emoji_message


main()