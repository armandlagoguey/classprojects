fire_detected = input("Is there a fire? (yes/no): ")
if fire_detected != "yes" and fire_detected != "no":
    print("Invalid input. Please enter 'yes' or 'no'.")
else:
    intrusion_detected = input("Is there an intrusion? (yes/no): ")
    if intrusion_detected != "yes" and intrusion_detected != "no":
        print("Invalid input. Please enter 'yes' or 'no'.")
    else:
        hour = int(input("Enter the current hour (0-23): "))
        if hour < 0 or hour > 23:
            print("Invalid hour. Please enter a valid hour.")
        else:
            if fire_detected == "yes":
                print("CRITICAL: Fire detected!")
            else:
                if intrusion_detected == "yes" and (hour < 8 or hour >= 18):
                    print("CRITICAL: Intrusion after hours!")
                elif intrusion_detected == "yes" and (8 <= hour < 18):
                    print("WARNING: Intrusion during working hours.")
                else:
                    print("SAFE: No issues")
