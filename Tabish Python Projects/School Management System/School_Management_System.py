
import pyttsx3

speaker = pyttsx3.init()

availableStd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
students = {}

print()
print("***********************")
print("*****   WELCOME   *****")
print("***********************")

def speak(sentence):
    speaker.say(sentence)
    speaker.runAndWait()

def new_record():
    speak('Enter Roll number')
    rollno = int(input('Enter Roll number: '))
    rollno = "%04d" % rollno
    if rollno in students.keys():
        speak('This Roll Number Already Exists')
        print('This Roll Number Already Exists')
        speak('Do you Want to try again enter y to try again or enter n to quit')
        yesno = input('Do you Want to try again y/n: ')

        if yesno == 'n' or yesno == 'N':
            speak('Thank you for using')
            print('Thank you for using')
            quit()
        elif yesno == 'y' or yesno == 'Y':
            new_record()
        else:
            speak('Invalid Input Thank you for using')
            print('Invalid Input Thank you for using')
            quit()
    else:
        speak('Enter Name of the Student')
        name = input('Enter Name of the Student: ')
        speak('Enter Class of the Student')
        std = int(input('Enter Class of the Student: '))
        if std not in availableStd:
            speak('Sorry we only have classes from first to tenth')
            print('Sorry we only have classes from I to X')
            speak('Thank you for using')
            print('Thank you for using')
            quit()
        else:
            std = "%02d" % std
            lst = []
            lst.append(std)
            lst.append(name)
            students[rollno] = lst

            with open('records.txt', 'a') as f:
                f.write('{ ' + str(rollno) + ' : '+ str(students[rollno]) + ' }\n')

            lst.clear()
            students.clear()
            speak('Record Added Successfully')
            print('Record Added Successfully')

            speak('Do you want to go to the Main Menu')
            yesno = input('Do you want to go to the Main Menu y/n: ')

            if yesno == 'n' or yesno == 'N':
                speak('Thank you for using')
                print('Thank you for using')
                quit()
            elif yesno == 'y' or yesno == 'Y':
                print('\n')
                main()
            else:
                speak('Invalid Input Thank you for using')
                print('Invalid Input Thank you for using')
                quit()

def display():
    with open('records.txt', 'r') as f:
        data = f.read()
    if data:
        print('\n')
        print('rollno = [standard,\'name\']')
        print(data)
        ('\n')
        speak('Do you want to go to the Main Menu')
        yesno = input('Do you want to go to the Main Menu y/n: ')
        if yesno == 'n' or yesno == 'N':
            speak('Thank you for using')
            print('Thank you for using')
            quit()
        elif yesno == 'y' or yesno == 'Y':
            print('\n')
            main()
        else:
            speak('Invalid Input Thank you for using')
            print('Invalid Input Thank you for using')
            quit()
    else:
        print('')
        speak('No Records Available Currently')
        print('No Records Available Currently')
        ('\n')
        speak('Do you want to go to the Main Menu')
        yesno = input('Do you want to go to the Main Menu y/n: ')
        if yesno == 'n' or yesno == 'N':
            speak('Thank you for using')
            print('Thank you for using')
            quit()
        elif yesno == 'y' or yesno == 'Y':
            print('\n')
            main()
        else:
            speak('Invalid Input Thank you for using')
            print('Invalid Input Thank you for using')
            quit()

def modify():
    speak('Enter Roll Number to Search for the record')
    rollno = "%04d" % int(input('Enter Roll Number to Search for the record: '))

    with open('records.txt','r') as f:
        for line in f.readlines():
            lst = []
            lst.append(line[11:13])
            lst.append(line[17:-5])
            students[line[2:6]] = lst

    if rollno in students.keys():
        speak('Record Exists')
        print('Record Exists')
        print('\n')
        print('rollno = [standard,\'name\']')
        print('{0} = {1}'.format(rollno,students[rollno]))
        print('\n')
        speak('Do You Want to Update this Record')
        yesno = input('Do You Want to Update this Record y/n: ')
        if yesno == 'n' or yesno == 'N':
            speak('Process Canceled Thank you for using')
            print('Process Canceled Thank you for using')
            quit()
        elif yesno == 'y' or yesno == 'Y':

            del students[rollno]

            speak('Enter new name of the Student')
            name = input('Enter new name of the Student: ')
            speak('Enter new class of the Student')
            std = int(input('Enter new class of the Student: '))
            if std not in availableStd:
                speak('Sorry we only have classes from first to tenth')
                print('Sorry we only have classes from I to X')
                speak('Thank you for using')
                print('Thank you for using')
                quit()
            else:
                std = "%02d" % std
                lst = []
                lst.append(std)
                lst.append(name)
                students[rollno] = lst

                with open('records.txt','w') as f:
                    for key, value in students.items():
                        f.write('{ ' + str(key) + ' : '+ str(value) + ' }\n')

                lst.clear()
                students.clear()
                speak('Record Updated Successfully')
                print('Record Updated Successfully')

            speak('Do you want to go to the Main Menu')
            yesno = input('Do you want to go to the Main Menu y/n: ')
            if yesno == 'n' or yesno == 'N':
                speak('Thank you for using')
                print('Thank you for using')
                quit()
            elif yesno == 'y' or yesno == 'Y':
                    print('\n')
                    main()
            else:
                speak('Invalid Input Thank you for using')
                print('Invalid Input Thank you for using')
                quit()
    else:
        speak('Record does not Exists')
        print('Record does not Exists')
        print('\n')
        speak('Do you want to go to the Main Menu')
        yesno = input('Do you want to go to the Main Menu y/n: ')
        if yesno == 'n' or yesno == 'N':
            speak('Thank you for using')
            print('Thank you for using')
            quit()
        elif yesno == 'y' or yesno == 'Y':
            print('\n')
            main()
        else:
            speak('Invalid Input Thank you for using')
            print('Invalid Input Thank you for using')
            quit()

def delete():
    speak('Enter Roll Number to Search for the record')
    rollno = "%04d" % int(input('Enter Roll Number to Search for the record: '))

    with open('records.txt','r') as f:
        for line in f.readlines():
            lst = []
            lst.append(line[11:13])
            lst.append(line[17:-5])
            students[line[2:6]] = lst

    if rollno in students.keys():
        speak('Record Exists')
        print('Record Exists')
        print('\n')
        print('rollno = [standard,\'name\']')
        print('{0} = {1}'.format(rollno,students[rollno]))
        print('\n')
        speak('Are You Sure You Want to delete this Record')
        yesno = input('Are You Sure You Want to Delete this Record y/n: ')
        if yesno == 'n' or yesno == 'N':
            speak('Process Canceled Thank you for using')
            print('Process Canceled Thank you for using')
            quit()
        elif yesno == 'y' or yesno == 'Y':
            del students[rollno]
            with open('records.txt','w') as f:
                for key, value in students.items():
                    f.write('{ ' + str(key) + ' : '+ str(value) + ' }\n')

            students.clear()
            speak('Record Deleted Successfully')
            print('Record Deleted Successfully')
            speak('Do you want to go to the Main Menu')
            yesno = input('Do you want to go to the Main Menu y/n: ')
            if yesno == 'n' or yesno == 'N':
                speak('Thank you for using')
                print('Thank you for using')
                quit()
            elif yesno == 'y' or yesno == 'Y':
                    print('\n')
                    main()
            else:
                speak('Invalid Input Thank you for using')
                print('Invalid Input Thank you for using')
                quit()
    else:
        speak('Record does not Exists')
        print('Record does not Exists')
        print('\n')
        speak('Do you want to go to the Main Menu')
        yesno = input('Do you want to go to the Main Menu y/n: ')
        if yesno == 'n' or yesno == 'N':
            speak('Thank you for using')
            print('Thank you for using')
            quit()
        elif yesno == 'y' or yesno == 'Y':
            print('\n')
            main()
        else:
            speak('Invalid Input Thank you for using')
            print('Invalid Input Thank you for using')
            quit()

def search():
    speak('Enter Roll Number to search for the record')
    rollno = int(input('Enter Roll Number to search for the record: '))
    rollno = "%04d" % rollno
    with open('records.txt','r') as f:
        for line in f.readlines():
            lst = []
            lst.append(line[11:13])
            lst.append(line[17:-5])
            students[line[2:6]] = lst

    if rollno in students.keys():
        speak('Record Exists')
        print('Record Exists')
        print('\n')
        print('{0} = {1}'.format(rollno,students[rollno]))
        print('\n')

        students.clear()
        
        speak('Do you want to go to the Main Menu')
        yesno = input('Do you want to go to the Main Menu y/n: ')
        if yesno == 'n' or yesno == 'N':
            speak('Thank you for using')
            print('Thank you for using')
            quit()
        elif yesno == 'y' or yesno == 'Y':
            print('\n')
            main()
        else:
            speak('Invalid Input Thank you for using')
            print('Invalid Input Thank you for using')
            quit()
    else:
        speak('Record does not Exists')
        print('Record does not Exists')
        print('\n')
        speak('Do you want to go to the Main Menu')
        yesno = input('Do you want to go to the Main Menu y/n: ')
        if yesno == 'n' or yesno == 'N':
            speak('Thank you for using')
            print('Thank you for using')
            quit()
        elif yesno == 'y' or yesno == 'Y':
            print('\n')
            main()
        else:
            speak('Invalid Input Thank you for using')
            print('Invalid Input Thank you for using')
            quit()

def main():
    print('')
    print('1: New Addmission')
    speak('enter 1 for new addmission.')
    print('2: Display Records')
    speak('enter 2 to display records')
    print('3: Update Record')
    speak('enter 3 to update record')
    print('4: Delete Record')
    speak('enter 4 to delete a record')
    print('5: Search Record')
    speak('enter 5 to search a record')
    print('6: Quit')
    speak('enter 6 to quit')
    print('')
    print('')
    speak('Enter your Choice')
    choice = int(input('Enter your Choice: '))

    if choice == 1:
        new_record()
    elif choice == 2:
        display()
    elif choice == 3:
        modify()
    elif choice == 4:
        delete()
    elif choice == 5:
        search()
    elif choice == 6:
        print('Thank you for using.')
        speak('Thank you for using')
        quit()
    else:
        print('Invalid Choice Try Again')
        speak('Invalid Choice Try Again')
        main()

main()

