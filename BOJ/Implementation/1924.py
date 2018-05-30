from datetime import date

x, y = map(int, input().split())
result = date(2007, x, y).weekday()

if result == 0:
    print("MON")
elif result == 1:
    print("TUE")
elif result == 2:
    print("WED")
elif result == 3:
    print("THU")
elif result == 4:
    print("FRI")
elif result == 5:
    print("SAT")
else:
    print("SUN")