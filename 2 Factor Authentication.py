import pyotp
import time

# Generate a new TOTP secret
def generate_secret():
    secret = pyotp.random_base32()
    print(f"Your secret is: {secret}")
    return secret

# Generate a TOTP token
def generate_token(secret):
    totp = pyotp.TOTP(secret)
    return totp.now()

# Verify a TOTP token
def verify_token(secret, token):
    totp = pyotp.TOTP(secret)
    return totp.verify(token)

if __name__ == "__main__":
    # Step 1: Generate a new secret key
    secret = generate_secret()

    # Step 2: Generate a TOTP token
    token = generate_token(secret)
    print(f"Your TOTP token is: {token}")

    # Step 3: Wait for user input to verify the token
    user_input = input("Enter the TOTP token to verify: ")

    # Step 4: Verify the entered token
    if verify_token(secret, user_input):
        print("Token is valid!")
    else:
        print("Token is invalid!")
