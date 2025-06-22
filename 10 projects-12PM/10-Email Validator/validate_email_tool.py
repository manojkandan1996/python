from email_validator import validate_email, EmailNotValidError

def check_email_format(email):
    try:
        valid = validate_email(email)
        print(f"✅ Valid format: {valid.email}")
        return True
    except EmailNotValidError as e:
        print(f"❌ Invalid format: {e}")
        return False

# Example
check_email_format("manojkandan1996@gmail.com")
check_email_format("god-email@")