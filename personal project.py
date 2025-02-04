work_file=open("hours.txt", "w")
days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for date in range(1,31, 6):
    total = 0
    print("Hours from", date, "to", date + 6, "December")
    work_file.write("Hours from "+str(date)+" to "+str(date+6)+" December\n")
    for day in days:
        hours=float(input(day+":"))
        total+=hours
        work_file.write(str(day)+":"+str(hours)+"\n")
    print("Total for this week is \n", total)
    work_file.write("Total for this week is "+str(total)+"\n\n")
work_file.close()
