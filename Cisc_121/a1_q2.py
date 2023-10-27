""""
CISC-121 2023W

Name:   <Joseph Liao>

Student Number: <20366481>

Email:  <22jl41@queensu.ca>

Date: 2023-01-16

I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity

"""
import random # imports the random module

# Open the file "myspace_profiles.txt" in append mode (a+)
f=open("myspace_profiles.txt",'a+')

# Write "Joseph Liao", 18, and "blue" to the file, with a newline after each value
f.write("Joseph Liao\n18\nblue\n-")

# Get user input for the name
name=input("Enter Name")

# Generate a random integer between 18 and 22 and assign it to the variable age
age=random.randint(18,22)

# Define a list of colors
list_of_colors=['green', 'red', 'yellow', 'pink', 'blue', 'orange']

# Get a random color from the list
color=list_of_colors[random.randint(0,5)]

# Write the name, age, color, and "-" to the file, with a newline character after each value
f.write("\n"+name+"\n"+str(age)+"\n"+color+"\n"+"-")

# Go to the start of the file
f.seek(0)

# Print the contents of the file
print(f.read())
