import pywhatkit

phone = input("enter phone number ")
msg = "today is a blessed day already"
pywhatkit.sendwhatmsg(phone, msg, 0, 49, 15, True, 2)
