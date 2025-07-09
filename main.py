from random import randint
from smtplib import *
from datetime import *
from Demos.win32ts_logoff_disconnected import username
now=datetime.now()
u="your_maild_id"
p="your_password"
from pandas import *
data=read_csv("birthdays.csv")
d=data.to_dict()
month=False
day=False
bithday_name=''
bithday_mail=''
for (key,value) in d.items():
    if key=="month":
        for (k,v) in d[key].items():
            if d[key][k] == now.month:

                month = True
    elif key=="day":
        for (k,v) in d[key].items():
            if d[key][k] == now.day:
                bithday_name=d["name"][k]
                bithday_mail=d["email"][k]

                day = True
    else:
        continue
if month==day:
    r=randint(1,3)
    with open(f"./letter_templates/letter_{r}.txt") as letter:
        old_content=letter.read()
        new_content=old_content.replace("[NAME]",bithday_name)
        # for gmail--smtp.gmail.com
        # for Yahoo--smtp.mail.yahoo.com
        c= SMTP("smtp.gmail.com",587)
        c.starttls()
        c.login(u,p)
        c.sendmail(from_addr=username, to_addrs=bithday_mail, msg=f"Subject:Happy Birthday\n\n{new_content}")
        c.close()








##################### Hard Starting Project ######################


# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



