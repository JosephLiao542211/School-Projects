def printMark(students,target_name):

    for p in range(len(students)):

        if students[p][0]==target_name:
            print("The marks for",students[p][0],"are:\n",
                  students[p][1][0],"%",
                  "For assignment #1 \n",students[p][1][1],"%",
                  "For assignment #2 \n",students[p][1][2],"%",
                  "For assignment #3 \n",students[p][1][3],"%",
                  "For assignment #4 \n")
            break
        if p==len(students)-1 and students[p]!=target_name:
            print("No student by the name of",target_name)

def averageAssignment(students,assignmentnum):

    totallist=[]
    for i in range(len(students)):
        totallist.append(students[i][1][assignmentnum])
    return round((sum(totallist))/len(totallist),2)



def averageMark(students,target_name):

    totalmarks=[]
    for p in range(len(students)):

        if students[p][0]==target_name:
            for marks in students[p][1]:
                totalmarks.append(marks)
            return (sum(totalmarks))/len(totalmarks)
        if p==len(students)-1 and students[p]!=target_name:
            return 0

def highestAverageMark(students):

    allmarks=[]
    higheststudents=[]
    for i in range(len(students)):
        allmarks.append(averageMark(students,students[i][0]))

    for i in range(len(students)):
        if max(allmarks)==averageMark(students, students[i][0]):
            higheststudents.append(students[i][0])

    return higheststudents


def increaseMarks(students):

    for i in range(len(students)):
        for x in range(len(students[i][1])):
            students[i][1][x] += 1


def addNewStudent(students):

    print("Add a new student>>")
    names=[]
    totalgrade=[]
    for i in range(len(students)):
        names.append(students[i][0])

    while True:
        name=input("please enter name of student")
        if name not in names:
             break

        print("try again")
    for i in range(4):
        while True:
            grade = int(input("please grade of assignment"+str(i+1)+":"))
            if grade in range(0,100):
                totalgrade.append(grade)
                break
            print("try again")

    profile=(name,totalgrade)
    students.append(profile)

def main():


    # leave the next 3 lines in your code.
    students = [("Jane", [80, 74, 93, 60]), ("Xinrong", [72, 89, 55, 75]), ("Sima", [93, 80, 74, 60])]
    print("Here is the data set", students)
    print("This program doesn't do anything yet.  Complete the program as per the comments ")

    # add lines of code that do the following:
    # call printMark() with name = "Xinrong"

    print("The following is the marks of Xingrong, Sima, and Joseph \n")
    printMark(students,"Xinrong")
    # call printMark() with name = "Sima"
    printMark(students, "Sima")
    # call printMark() with your own name
    printMark(students, "Joseph")

    # call averageAssignment()for the assignment 1 (the first mark for each student)
    # print the average that was returned by averageAssignment()

    print("The following is the average marks of Assignment 1 for all students \n")
    print(averageAssignment(students,0),"%")

    # call averageMark to get Jane's overall average

    print("\nThe following is the average marks of Jane and Tom \n")
    print("Jane's average is",averageMark(students,"Jane"))
    # call averageMark for a student who does not exist
    print("Tom's average is", averageMark(students, "Tom"))

    # print the name(s) of the student(s) with the highest average. Be user friendly!  Do not
    # just print the list like this:  ["ab", "cd"].

    print("\nThe following is the students with the highest marks \n")
    thebest=highestAverageMark(students)
    print("The people with the highest grade are:")
    for person in (thebest):
        print(person)

    print("\nTo insert a new student into the list please follow the prompt\n")

    #allow the user to add a new student
    addNewStudent(students)

    print("\nThe following is the new list of students \n")
    # leave this in your code so that we can see the new student list.
    print(students)

    print("\nThe following is the new list of students and their marks with a 1% increase\n")
    # increase the marks
    increaseMarks(students)

    # leave this so that we can see the change in the marks.
    print(students)


main()