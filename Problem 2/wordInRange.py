def wordInRange():
    filename = input()
    first_char = input()
    second_char = input()
    wordlist = open(filename, 'r').readlines()
    wordlist2 = []
    for i in range(0, len(wordlist)):
        newterm = wordlist[i].strip()
        wordlist2.append(newterm)
    for i in range(0, len(wordlist2)):
        if wordlist2.index(f"{first_char}") <= i <= wordlist2.index(f"{second_char}"):
            print(f"{wordlist2[i]} - in range")
        else:
            print(f"{wordlist2[i]} - not in range")
    

if __name__ == '__main__':
    wordInRange()
    