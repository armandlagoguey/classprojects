audit_log = open('audit_log.txt', "w")

msg1 = input("Type the first message :")
msg2 = input("Type the second message :")
msg3 = input("Type the third message :")

msg1 = msg1.lower()
msg2 = msg2.lower()
msg3 = msg3.lower()

if msg1 in ("critical") or msg1 in ("e101"):
    audit_log.write(f"LOGGED: {msg1}\n")
else:
    print("Message filtered and discarded")

if msg2 in ("critical") or msg2 in ("e101"):
    audit_log.write(f"LOGGED: {msg2}\n")
else:
    print("Message filtered and discarded")

if msg3 in ("critical") or msg3 in ("e101"):
    audit_log.write(f"LOGGED: {msg3}\n")
else:
    print("Message filtered and discarded")

audit_log.close()
