"""
Name: Henry Holman
Lab time: thursday 2 pm
"""


def wordInRange():
    filename = input()
    first_char = input()
    second_char = input()
    wordlist = open(filename, 'r').readlines()
    wordlist2 = []
    for i in range(0, len(wordlist)):
        newterm = wordlist[i].strip()
        wordlist2.append(newterm)
    for i in wordlist2:
        if first_char <= i <= second_char:
            print(f"{i} - in range")
        else: 
            print(f"{i} - not in range")
   

if __name__ == '__main__':
    wordInRange()
    