print("Enter 1 to add a school subject to the text file.")
print("Enter 2 to display the contents of the file.")
print("Enter 3 to do all of the above.")
user_ans = input("Entry:")

#run the lines below if the file doesn't exist yet:
'''
subjects1 = open("Subject.txt", "x")
subjects1.close()
'''
if user_ans == "1":
    subjects2 = open("Subject.txt", "w")
    new_sub = input("Enter a new subject: ")
    subjects2.write(new_sub)
    subjects2.close()
elif user_ans == "2":
    subjects3 = open("Subject.txt", "r")
    print(subjects3.read())
    subjects3.close()
elif user_ans ==  "3":
    subjects4 = open("Subject.txt", "r+")
    new_sub = input("Enter a new subject: ")
    subjects4.write(new_sub)
    print(subjects4.read())
    subjects4.close()
    subjects5 = open("Subject.txt", "r")
    print(subjects5.read())
    subjects5.close()
    

else:
    print("Error.")