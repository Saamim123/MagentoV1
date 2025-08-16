
import random
import string

def generate_random_email():
    username= ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain= "gmail.com"
    return f"{username}@{domain}"


