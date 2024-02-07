def toNumber(roman):
    roman = roman.upper()
    dict = {
          "I": 1,
          "V": 5,
          "X": 10,
          "L": 50,
          "C": 100,
          "D": 500,
          "M": 1000,
    }

    total = 0

    for i in range(len(roman)):
        if i < len(roman) - 1 and dict[roman[i]] < dict[roman[i + 1]]:
            total -= dict[roman[i]]
        else:
            total += dict[roman[i]]

    print(total)

def main():
    toNumber("MCMVII")
    toNumber("MMXI")
    toNumber("XC")
    toNumber("MCMXC")
    toNumber("MCMX")
    toNumber("MCmxCII")
    toNumber("dVl")

main()
