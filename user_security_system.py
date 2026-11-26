print("========================================")
print("           CYBERGUARD v1.0")
print()
print("   PERSONAL SECURITY MONITORING SYSTEM")
print("========================================")
print()
print("Welcome, Security Analyst!")
print()
print("Your mission is to monitor account")
print("information and identify potential threats.")
print()
print("Starting security assessment...")

user_name = str(input("Enter your username: "))
user_email = str(input("Enter your email address: "))
user_password = str(input("Enter password: "))
user_age = int(input("Enter your age: "))
user_ip = str(input("Enter your current IP address: "))
fail_attempt = int(input("Failed login attepmts: "))
account_status = input("Is this account active or inactive? ")

if account_status.lower() == 'active':
    account_status = True
else:
    account_status = False

#User input feedback
if fail_attempt == 0:
    print("No failed login attempts detected")

if fail_attempt >=1 and fail_attempt <= 4:
    print("Low security alert")

if fail_attempt >= 5:
    print("Critical warning: Possible brute-force attack")


print()
print()

if account_status == False:
    print("Account access is currently disable")

if account_status == True and fail_attempt < 5:
    print("No critical login threat detected")


if len(user_password) < 8:
    print("Weak Password")

if len(user_password) >= 8 and len(user_password) <= 11:
    print("Moderate password")

if len(user_password) >= 12:
    print("Strong password")

print()
print()

#Report generation
print()
print("========================================")
print("       CYBERGUARD SECURITY REPORT")
print("========================================")
print()
print("USER INFORMATION")
print("----------------------------------------")
print(f"Username: {user_name}")
print(f"Email: {user_email}")
print(f"Age: {user_age}")
print(f"IP Address: {user_ip}")

if account_status == True:
    print("Account Status: ACTIVE")
else:
    print("Account Status: INACTIVE")


print()
print("SECURITY ANALYSIS")
print("----------------------------------------")

if len(user_password) < 8:
    print("Password Assessment: WEAK")

elif len(user_password) >= 8 and len(user_password) <= 11:
    print("Password Assessment: MODERATE")

elif len(user_password) >= 12:
    print("Password Assessment: STRONG")

print(f"Failed Login Attempts: {fail_attempt}")
print()

print("THREAT DETECTION")
print("----------------------------------------")

if fail_attempt == 0:
    print("[SAFE] No threats detected.")

elif fail_attempt >=1 and fail_attempt <= 4:
    print("[CAUTION] A few log in attemps detected.")

elif fail_attempt >= 5:
    print("[CRITICAL] Multiple failed login attempts!")
    print("[WARNING] Possible brute-force attack detected.")


print()
print("FINAL SECURITY STATUS")
print("----------------------------------------")

if fail_attempt == 0:
    print("THREAT LEVEL: SECURE")

elif fail_attempt >=1 and fail_attempt <= 4:
    print("THREAT LEVEL: LOW")

elif fail_attempt >= 5:
    print("THREAT LEVEL: HIGH")

print()
print("RECOMMENDATION:")

if fail_attempt == 0:
    print("No action required.")

elif fail_attempt >=1 and fail_attempt <= 4:
    print("Possible misinputs. Review recent activity")
    print("and update password if necessary.")

elif fail_attempt >= 5:
    print("Investigate the login activity and secure")
    print("the account immediately")


print("========================================")
print("         END OF SECURITY REPORT")
print("========================================")
