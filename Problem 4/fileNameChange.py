"""
Name: Henry Holman
Lab Time: Thursday 2 pm
"""


def fileNameChange():
    #get input

    program = input("input program name\n")
    with open(program, "r") as photolist:
        name_file = photolist.readlines()
        for line in range(0, len(name_file)):
            image_name = name_file[line].split("_")[0]
            new_file_name = f"{image_name}_info.txt"
            print(new_file_name)
            


    return

if __name__ == '__main__':
    fileNameChange()