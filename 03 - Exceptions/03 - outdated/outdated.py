months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    
    date = input("Date: ")


    if "/" in date:
        try:
            day, month, year = date.split("/")
        except ValueError:
            continue
        else:
            day, month, year = int(day), int(month), int(year)
            if day >= 0 and day <= 31 | month > 0 and month <= 12:
                print(f"{year}" f"-{month:02}" f"-{day:02}")
                break


    elif " " in date:
        try:
            month, day, year = date.split(" ")
        except ValueError:
            continue
        else:
            # Add comma condition also
            if month in months:
                month = months.index(month, 0, 12) + 1
                day = day.replace(",", "")
                month, day, year = int(month), int(day), int(year)
                
                if day >= 0 and day <= 31 | month > 0 and month <= 12:
                    print(f"{year}" f"-{month:02}" f"-{day:02}")
                    break

            










        