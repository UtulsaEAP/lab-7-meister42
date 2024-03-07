"""
Name: Henry Holman
Lab time: thursday 2pm

"""



def exceptionHandling():
    # Split input into 2 parts: name and age
    parts = input().split()
    name = parts[0]
    
    while name != '-1':
        try :
            age = int(parts[1]) + 1
            print(f'{name} {age}')
        except :
            age = 0
            print(f'{name} {age}')
        # Get next line
        parts = input().split()
        name = parts[0]


if __name__ == '__main__':
    exceptionHandling()