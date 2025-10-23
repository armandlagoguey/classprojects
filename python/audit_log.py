audit_log = open('audit_log.txt', "w")



msg1 = input("Type the first message :")
msg2 = input("Type the second message :")
msg3 = input("Type the third message :")

msg1 = msg1.lower()
msg2 = msg2.lower()
msg3 = msg3.lower()

if ("critical") in msg1 or ("e101") in msg1:
    audit_log.write(f"LOGGED: {msg1}\n")
else:
    print("Message filtered and discarded")

if ("critical") in msg2 or ("e101") in msg2:
    audit_log.write(f"LOGGED: {msg2}\n")
else:
    print("Message filtered and discarded")

if ("critical") in msg3 or ("e101") in msg3:
    audit_log.write(f"LOGGED: {msg3}\n")
else:
    print("Message filtered and discarded")

audit_log.close()
