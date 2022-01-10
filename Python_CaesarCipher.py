def input_encryption():
    encryption = input("Encryption (E) or Decryption (D): ")
    while encryption.upper() != 'E' and encryption.upper() != 'D':
        encryption = input("Enter E for Encryption or D for Decryption: ")
    return encryption.upper()

def set_encryption():
    encryption = input_encryption()
    if encryption == 'E':
        return True
    else:
        return False

def input_language():
    language = input("English (ENG) or Russian (RUS): ")
    while language.upper() != 'ENG' and language.upper() != 'RUS':
        language = input("Enter ENG for English or RUS for Russian: ")
    return language.upper()

def set_language():
    language = input_language()
    if language == 'ENG':
        return 26
    else:
        return 32

def set_shift():
    shift = input("Enter number for the shift: ")
    while not shift.isnumeric():
        shift = input("Enter number for the shift: ")
    return int(shift)

def input_hack():
    is_hack = input("Hack the cipher? (Y/N): ")
    while is_hack.upper() != 'Y' and is_hack.upper() != 'N':
        is_hack = input("Enter Y for Yes or N for No: ")
    return is_hack.upper()

def set_hack():
    is_hack = input_hack()
    if is_hack == 'Y':
        return True
    else:
        return False

def set_options():
    is_encryption = set_encryption()
    amount_symbols = set_language()

    if not is_encryption:
        is_hack = set_hack()
    else:
        is_hack = False
    
    if is_hack:
        shift = 1
    else:
        shift = set_shift()
        shift %= amount_symbols

    return is_encryption, amount_symbols, shift, is_hack

def encryption(text, amount_symbols, shift):
    encryption_text = ''
    amount_english = 26
    amount_russian = 32

    if amount_symbols == amount_english:
        symbol_begin = 'a'
        symbol_end = 'z'
    else:
        symbol_begin = 'а'
        symbol_end = 'я'

    for symbol in text:
        if symbol.islower():
            symbol_begin = symbol_begin.lower()
            symbol_end = symbol_end.lower()
        else:
            symbol_begin = symbol_begin.upper()
            symbol_end = symbol_end.upper()

        if symbol >= symbol_begin and symbol <= symbol_end:
            if ord(symbol) + shift > ord(symbol_end):
                encryption_text += chr(ord(symbol_begin) - 1 + (shift - (ord(symbol_end) - ord(symbol))))
            else:
                encryption_text += chr(ord(symbol) + shift)
        else:
            encryption_text += symbol
    return encryption_text

def decryption(text, amount_symbols, shift):
    decryption_text = ''
    amount_english = 26
    amount_russian = 32

    if amount_symbols == amount_english:
        symbol_begin = 'a'
        symbol_end = 'z'
    else:
        symbol_begin = 'а'
        symbol_end = 'я'

    for symbol in text:
        if symbol.islower():
            symbol_begin = symbol_begin.lower()
            symbol_end = symbol_end.lower()
        else:
            symbol_begin = symbol_begin.upper()
            symbol_end = symbol_end.upper()

        if symbol >= symbol_begin and symbol <= symbol_end:
            if ord(symbol) - shift < ord(symbol_begin):
                decryption_text += chr(ord(symbol_end) + 1 - (shift - (ord(symbol) - ord(symbol_begin))))
            else:
                decryption_text += chr(ord(symbol) - shift)
        else:
            decryption_text += symbol
    return decryption_text

def caesar_cipher():
    is_encryption, amount_symbols, shift, is_hack = set_options()
    text = input("Enter your text: ")

    if is_hack:
        while shift < amount_symbols:
            result = decryption(text, amount_symbols, shift)
            print(result)
            shift += 1

    if is_encryption:
        result = encryption(text, amount_symbols, shift)
    else:
        result = decryption(text, amount_symbols, shift)
    print(result)

caesar_cipher()
