"""
Name: Henry Holman
Lab Time: thursday 2 pm

"""


def courseGrade():
    
    # TODO: Declare any necessary variables here. 
    filename = input()
    firstname = []
    lastname = []
    midterm1 = []
    midterm2 = []
    final = []
    grade = []

    # TODO: Read a file name from the user and read the tsv file here. 
    
    studentinfo =  open(filename, 'r').readlines()

    specificstudent = []
    for i in range(0, len(studentinfo)):
        specificstudent = studentinfo[i].split()
        firstname.append(specificstudent[1])
        lastname.append(specificstudent[0])
        midterm1.append(int(specificstudent[2]))
        midterm2.append(int(specificstudent[3]))
        final.append(int(specificstudent[4]))
        specificaverage = (int(midterm1[i])+int(midterm2[i])+int(final[i]))/3
        if specificaverage >= 90:
            grade.append("A")
        elif specificaverage >= 80:
            grade.append("B")
        elif specificaverage >= 70:
            grade.append("C")
        elif specificaverage >= 60:
            grade.append("D")
        else:
            grade.append("F")

    midterm1_avg = sum(midterm1)/len(midterm1)
    midterm2_avg = sum(midterm2)/len(midterm2)
    final_avg = sum(final)/len(final)
    #output data into correct report file
    if "1" in str(filename):
        with open("report1.txt", "w") as outputfile:
            for i in range(0, len(studentinfo)):
                outputfile.write(f"{lastname[i]}\t{firstname[i]}\t{midterm1[i]}\t{midterm2[i]}\t{final[i]}\t{grade[i]}\n")
            outputfile.write(f"\nAverages: midterm1{midterm1_avg: .2f}, midterm2{midterm2_avg: .2f}, final{final_avg: .2f}")
        open("report1.txt", "r")
    elif "2" in str(filename):
        with open("report2.txt", "w") as outputfile:
            for i in range(0, len(studentinfo)):
                outputfile.write(f"{lastname[i]}\t{firstname[i]}\t{midterm1[i]}\t{midterm2[i]}\t{final[i]}\t{grade[i]}\n")
            outputfile.write(f"\nAverages: midterm1{midterm1_avg: .2f}, midterm2{midterm2_avg: .2f}, final{final_avg: .2f}")
        open("report2.txt", "r")
    else:
        with open("report.txt", "w") as outputfile:
            for i in range(0, len(studentinfo)):
                outputfile.write(f"{lastname[i]}\t{firstname[i]}\t{midterm1[i]}\t{midterm2[i]}\t{final[i]}\t{grade[i]}\n")
            outputfile.write(f"\nAverages: midterm1{midterm1_avg: .2f}, midterm2{midterm2_avg: .2f}, final{final_avg: .2f}")
        open("report.txt", "r")

 
    return

if __name__ == "__main__":
    courseGrade()
    
    