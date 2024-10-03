import sys

braille_map = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    " ": "......",
    "capital": ".....O",
    "number": ".O.OOO"
}
reverse_braille_map = {v: k for k, v in braille_map.items()}

def detect_input_type(input_string):
    if all(c in "O." for c in input_string):
        return "braille"
    else:
        return "english"

def translate_to_braille(text):
    braille_output = []
    number_mode = False

    for char in text:
        if char.isupper():
            braille_output.append(braille_map["capital"])
            char = char.lower()

        if char.isdigit():
            if not number_mode:
                braille_output.append(braille_map["number"])
                number_mode = True
        else:
            number_mode = False

        braille_output.append(braille_map.get(char, "......"))

    return ''.join(braille_output)

def translate_to_english(braille):
    english_output = []
    number_mode = False
    i = 0
    while i < len(braille):
        symbol = braille[i:i + 6]
        if symbol == braille_map["capital"]:
            next_char = braille[i + 6:i + 12]
            english_output.append(reverse_braille_map.get(next_char, "?").upper())
            i += 12
        elif symbol == braille_map["number"]:
            number_mode = True
            i += 6
        else:
            char = reverse_braille_map.get(symbol, "?")
            if number_mode and char.isdigit():
                english_output.append(char)
            else:
                number_mode = False
                english_output.append(char)
            i += 6

    return ''.join(english_output)


if __name__ == "__main__":

    input_string = ' '.join(sys.argv[1:])

    input_type = detect_input_type(input_string)

    if input_type == "english":
        result = translate_to_braille(input_string)
    elif input_type == "braille":
        result = translate_to_english(input_string)

    print(result)

