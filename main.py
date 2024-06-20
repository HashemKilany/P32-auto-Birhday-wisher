##################### Hard Starting Project ######################
import random
from datetime import datetime as dt
import pandas as pd
import smtplib

my_email = "hashemgiza717@gmail.com"
ps = "lzolqlpatcjisgzh"

today = dt.now()
today_tuple = (today.year, today.month, today.day)
data = pd.read_csv("birthdays.csv")
birthdays_dict = {data_row["id"]: data_row for (index, data_row) in
                  data.iterrows()}
for birthday in birthdays_dict.values():
    if (today_tuple[1] == birthday["month"]) & (today_tuple[2] == birthday["day"]):
        letter_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(letter_path) as letter:
            content = letter.read()
            content = content.replace("[NAME]", birthday["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=ps)
            connection.sendmail(from_addr=my_email, to_addrs=f"{birthday.email}",
                                msg=f"Subject:Happy Birthday!\n\n{content}")

