import random

# List of names
names_list = ["Anirudh", "Akash", "Akshay", "Ashwath", "Karthick", "Koushik", "Lokesh", "Pranav", "Vikram",
              "Aditi", "Aishwarya", "Akshara", "Anjana", "Anusha", "Aparna", "Archana", "Bhavya", "Bhavana",
              "Bhumika", "Divya", "Janani", "Kavya", "Kavita", "Mahima", "Meghana", "Nikitha", "Ramya",
              "Ritikha", "Sahana", "Saranya", "Sushmitha", "Sanjana", "Tanya", "Vaishnavi"]

# Function to generate email addresses
def generate_email(name):
    domains = ["gmail.com", "mail.com", "yahoo.com", "orkut.com"]
    domain = random.choice(domains)
    return f"{name.lower()}.{random.randint(1, 100)}@{domain}"

# Generate email addresses for each name
realistic_emails = [generate_email(name) for name in names_list]

# Print the generated email addresses
for email in realistic_emails:
    print(email)