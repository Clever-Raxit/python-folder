day = ""

monday = "\n{Monday subject = Maths,\n\n7:30 to 8:30am read the subject,\n9:30am to 11:00pm live class if,\n1:00 to 4:00 worksheet,\n6:00 to 7:30 practice computer}\n"

tuesday = "\n{Tuesday subject = S.S,\n\n7:30 to 8:30am read the subject,\n9:30am to 11:00pm live class if,\n1:00 to 4:00 worksheet,\n6:00 to 7:30 practice computer}\n"

wednesday = "\n{Wednesday subject = Science,\n\n7:30 to 8:30am read the subject,\n9:30am to 11:00pm live class if,\n1:00 to 4:00 worksheet,\n6:00 to 7:30 practice computer}\n"

thursday = "\n{Thursday subject = English,\n\n7:30 to 8:30am read the subject,\n9:30am to 11:00pm live class if,\n1:00 to 4:00 worksheet,\n6:00 to 7:30 practice computer}\n"

friday = "\n{Friday subject = Gujarati,\n\n7:30 to 8:30am read the subject,\n9:30am to 11:00pm live class if,\n1:00 to 4:00 worksheet,\n6:00 to 7:30 practice computer}\n"

saturday = "\n{Saturday subject = Sanskrit,\n\n7:30 to 8:30am read the subject,\n9:30am to 11:00pm live class if,\n1:00 to 4:00 worksheet,\n6:00 to 7:30 practice computer}\n"

sunday = "\n{Sunday subject = Computer,\n\n7:30 to 8:30am read the subject,\n9:30am to 11:00pm do anything,\n1:00 to 3:00 sleep, 4:30 watch t.v or tutorial}\n"

day = input("Enter which day you want: ")
if day == "monday":
    print(monday)
elif day == "tuesday":
    print(tuesday)
elif day == "wednesday":
    print(wednesday)
elif day == "thursday":
    print(thursday)
elif day == "friday":
    print(friday)
elif day == "saturday":
    print(saturday)
else:
    print(sunday)
