eng_to_kan = {
    '0': '೦',
    '1': '೧',
    '2': '೨',
    '3': '೩',
    '4': '೪',
    '5': '೫',
    '6': '೬',
    '7': '೭',
    '8': '೮',
    '9': '೯'
}

def english_to_kannada_number(num_str):
    """Convert English number string to Kannada number string"""
    kannada_num = ""
    for ch in num_str:
        if ch in eng_to_kan:
            kannada_num += eng_to_kan[ch]
        else:
            kannada_num += ch
    return kannada_num

number = input("Enter a number in English digits: ")
converted = english_to_kannada_number(number)
print("Kannada number:", converted)
