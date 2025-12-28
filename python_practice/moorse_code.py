MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
result = ""
decoded = []
choice = input("What do you want to do?\nCipher: stores the morse translated form of the english string\ndecipher: stores the english translated form of the morse string\n").lower()
if choice in ['decipher', 'cipher']:
    if choice == 'decipher':
        string_input = input("Please type your string to decipher the string: ")
        values = string_input.split()
        for morse in values:
            for key, value in MORSE_CODE_DICT.items():
                if value == morse:
                    decoded.append(key)
                    break
        result = "".join(decoded)
    else:
        string_input = input("Please type your string to cipher the string: ")
        result = " ".join(
            MORSE_CODE_DICT.get(ch.upper(), "")
            for ch in string_input
            if ch != " "
        )
    print(result)
