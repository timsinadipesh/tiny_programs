# converts a given number to roman numerals

def to_roman_numeral(num):
    if not 1 <= num <= 3999:
        return "Number must be between 1 and 3999 inclusive."
    
    roman_numerals = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
    result = ""
    for value, numeral in roman_numerals.items():
        while num >= value:
            result += numeral
            num -= value 
    return result


print(1, ":", to_roman_numeral(1))
print(2, ":", to_roman_numeral(2))
print(4, ":", to_roman_numeral(4))
print(8, ":", to_roman_numeral(8))
print(16, ":", to_roman_numeral(16))
print(32, ":", to_roman_numeral(32))
print(64, ":", to_roman_numeral(64))
print(128, ":", to_roman_numeral(128))
print(256, ":", to_roman_numeral(256))
print(512, ":", to_roman_numeral(512))
print(1024, ":", to_roman_numeral(1024))
print(2048, ":", to_roman_numeral(2048))
print(4096, ":", to_roman_numeral(4096))