import datetime as d

age = int(input('What is your age? '))
retire_age = int(input('At what age would you like to retire? '))

yrs_to_retirement = retire_age - age
curr_year = d.date.today().year

print(f"\nIt's {curr_year}. You will retire in {curr_year + yrs_to_retirement}"
      f"\nYou have only {yrs_to_retirement} years of work to go!")