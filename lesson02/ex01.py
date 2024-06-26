def email_validation_check(email):
    if '@' not in email:
        raise ValueError("the Email must have @ in it", email)
    return email

emails = ["alieisami@gmail.com","ali_gmail.com","email.co.il","email@email.com"]

for email in emails:
    try:
        print(email_validation_check(email), "Valid Email")
    except ValueError as e:
        print("Caught an exception:", e)