### You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. 
### At what time does the alarm go off?
### Write a Python program to solve the general version of the above problem. 
### Ask the user for the time now (in hours), and ask for the number of hours to wait. 
### Your program should output what the time will be on the clock when the alarm goes off.

def alarm_clock():

    while True:
        timenow = input("Enter the current time (hh:mm): " )
        tn = timenow.split(":")
        if len(tn) == 2:
            try:
                hour = int(tn[0])
                minute = int(tn[1])
                if hour >= 0 and minute >= 0:
                    if hour < 24 and minute < 60:
                        break
                    else:
                        print("There are only 24 hours in a day and 60 minutes in a hour!")
                else:
                    print("Provide two positive integers!")
            except:
                print("Provide two positive integers in the correct format!")
        else:
            print("Time in the wrong format!")

    print("The current time is: {0:02d}:{1:02d}".format(hour, minute))

    while True:
        hours_to_wait = int(input("Enter the amount of hours to wait: "))
        if hours_to_wait < 0:
            print("It can't be a negative number, unless you have a time travel machine!")
        else:
            break

    reminder = hours_to_wait % 24

    following_days = (hours_to_wait // 24) + ((hour + reminder) // 24)

    alarmTime = (hour + reminder) % 24

    init_str = "The alarm will go off at "

    if following_days == 0:
        print(init_str + "{0:02d}:{1:02d} today".format(alarmTime, minute))
    elif following_days == 1:
        print(init_str + "{0:02d}:{1:02d} tomorrow".format(alarmTime, minute))
    else:
        print(init_str + "{0:02d}:{1:02d} in {2} days".format(alarmTime, minute, following_days))

if __name__ == "__main__":
    alarm_clock()