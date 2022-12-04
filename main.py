morse_code_dict = {
    "a": "·−", "b": "-···", "c": "-·-·", "d": "-··", "e": "·", "f": "··-·", "g": "--·", "h": "····", "i": "··",
    "j": "·---", "k": "-·-", "l": "·-··", "m": "--", "n": "-·", "o": "---", "p": "·--·", "q": "--·-", "r": "·-·",
    "s": "···", "t": "-", "u": "··-", "v": "···-", "w": "·--", "x": "-··-", "y": "-·--", "z": "--··", "0": "-----",
    "1": "·----", "2": "··---", "3": "···--", "4": "····-", "5": "·····", "6": "-····", "7": "--···", "8": "---··",
    "9": "----·", " ": "  ", ".": "·-·-·-", ",": "--··--", "?": "··--··",
}

print("Welcome to Text-To-Morse converter.")

keep_coding = True

while keep_coding:
    text = input("Type in the text you'd like to code: \n")
    output = ""

    for element in text.lower():
        try:
            coded_element = morse_code_dict[element]
        except KeyError:
            pass
        else:
            output += coded_element + " "
    print(output)

    response = input("Would you like to continue? Type 'y' or 'n': ")
    if response == 'n':
        keep_coding = False
