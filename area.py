def leap_year(year):
    if(year%4)==0:
        if(year%100)==0:
            if(year%400)==0:
                print("{0} is a leap year".format(year))
            else:
                print("{0} is a not a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is a not a leap year".format(year))
    
year=int(input("Enter a year:"))
leap_year(year)
