# -- Canadian Business College -- FSWD -- Python Fundamentals Assignment.1 --

# declaring our initial value (number of courses completed by our user) and getting it from the user as an input
num_of_courses = int(input("How many courses have you finished? "))

print("Good job on successfully completing " + str(num_of_courses) + " courses!")

courses_marks = []

# Let's make a while loop that will run for as long as the value of our counter is not higher than num_of_courses
count = 1

while count <= num_of_courses:

# Use .append() method to add user's input (marks for each course) to our empty list courses_marks []		
	courses_marks.append(int(input("Please enter your mark for the course #" + str(count) + " ? ")))
	count += 1	
	 
	total = 0
	average = 0

# Let's iterate over our marks to get a sum and their aberage	
for num in courses_marks :
	total += num
	
average = round((total / num_of_courses), 2)

print("Your average mark for this semester is: " + str(average))
	
# Use an if..elif statement to determine what's our user's grade
if (average >= 90 and average <=100):
	print("Excellent job! Your grade is A+")
				 
elif (average >= 80 and average <=89):
	print("Good job! Your grade is B")
			 
elif (average >= 70 and average <=79):
	print("Please put more effort next time! Your grade is C")
			 
elif (average >=60 and average <=69):
	print("Keep working! Your grade is D")
			 
elif average <60 :
	print("Your grade is F")

# -- All DONE -- I have tested my code in VS Code Terminal window as well as in my Command Line with Geany. 
# The code is working an intended 

		 
			
	
