import smtplib
import datetime as dt
import pandas as pd

my_email=os.environ.get("MY_EMAIL")
password=os.environ.get("MY_PASSWORD")
##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 
now = dt.datetime.now()
# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.

# HINT 2: You could create a dictionary from birthdays.csv that looks like this:


df = pd.read_csv('birthdays.csv')

# 'records' format: list of dictionaries [{col1: val1, col2: val2}, ...]
birthdays_dict =  df.to_dict(orient='records')
print(birthdays_dict)
with open('letter_templates/letter_1.txt', 'r') as file:
    content = file.read()

for d in birthdays_dict:
    if d['month'] == now.month and d['day'] == now.day:
        new_content = content.replace('[NAME]',d['name'])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=d['email'],
                msg=f'Subject:Happy Birthday\n\n{new_content}'
            )
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



