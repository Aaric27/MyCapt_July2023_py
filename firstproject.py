import csv 

def csv_input(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number", "Email Id"])
        writer.writerow(info_list)
if __name__ ==  '__main__':
    condition = True
    student_num = 1

    while (condition):
        student_info=input("Enter the student information for student #{} in this particular format (Name Age Contact_Number Email_id): ".format(student_num)  )
        print("Entered student information: ", student_info)

        student_info_list = student_info.split(' ')
        print("Entered split up information is: " + str(student_info_list))
        print("\nThe entered information is -\nName: {}\nAge: {}\nContact number: {}\nEmail ID: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))


        correct = input("Is the information you inputted correct? (yes/no): ")
        if correct == "yes":

        
            csv_input(student_info_list)

            condition_check = input("Input yes if you want to add another student's information or input no if you are done: ")
            if condition_check == "yes":
                condition = True
                student_num = student_num+1
            elif condition_check == "no" :
                condition = False
        elif correct == "no":
            print("\nPlease re-enter the values")