import pytz

with open("timezones.txt", "w") as f:
    for i in pytz.all_timezones:
        f.write("#")
        f.write(i)
        f.write("\n")