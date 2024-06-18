import pandas as pd
import numpy as np
import random
from bs4 import BeautifulSoup

# Load the existing Excel file content as HTML
with open('./profiles_240609_1840.xls', 'r') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table')

# Read the table into a DataFrame
df_existing = pd.read_html(str(table))[0]

# Generate lists of generic data
generic_names = ["John Smith", "Emily Johnson", "Michael Brown", "Sarah Davis", "David Miller", 
                   "Jessica Wilson", "James Taylor", "Jennifer Moore", "Robert Anderson", "Linda Thompson",
                   "William Jackson", "Elizabeth White", "Charles Harris", "Mary Martin", "Christopher Lee",
                   "Patricia Walker", "Daniel Young", "Barbara King", "Matthew Wright", "Susan Scott",
                   "Anthony Green", "Margaret Adams", "Joseph Hall", "Karen Nelson", "Mark Carter"]

generic_emails = ["john.smith@gmail.com", "emily.johnson@yahoo.com", "michael.brown@hotmail.com",
                    "sarah.davis@outlook.com", "david.miller@mail.com", "jessica.wilson@gmail.com",
                    "james.taylor@yahoo.com", "jennifer.moore@hotmail.com", "robert.anderson@outlook.com",
                    "linda.thompson@mail.com", "william.jackson@gmail.com", "elizabeth.white@yahoo.com",
                    "charles.harris@hotmail.com", "mary.martin@outlook.com", "christopher.lee@mail.com",
                    "patricia.walker@gmail.com", "daniel.young@yahoo.com", "barbara.king@hotmail.com",
                    "matthew.wright@outlook.com", "susan.scott@mail.com", "anthony.green@gmail.com",
                    "margaret.adams@yahoo.com", "joseph.hall@hotmail.com", "karen.nelson@outlook.com",
                    "mark.carter@mail.com"]
generic_locations = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio",
                       "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus",
                       "Charlotte", "San Francisco", "Indianapolis", "Seattle", "Denver", "Washington"]


# Function to generate random data points similar to existing ones
def generate_similar_data(df, num_new_points):
    new_data = []
    for i in range(num_new_points):
        new_point = {}
        new_point["ID"] = df["ID"].max() + i + 1  # Auto-increment ID
        for column in df.columns:
            if column == 'Name':
                new_point[column] = random.choice(generic_names)
            elif column == 'Mail ID':
                new_point[column] = random.choice(generic_emails)
            elif column == 'Preferred Gym Location':
                new_point[column] = random.choice(generic_locations)
            elif pd.api.types.is_numeric_dtype(df[column]):
                # Generate a number within the range of existing values
                min_val = df[column].min()
                max_val = df[column].max()
                if pd.api.types.is_integer_dtype(df[column]):
                    new_point[column] = random.randint(min_val, max_val)
                else:
                    new_point[column] = round(random.uniform(min_val, max_val), 2)
            elif pd.api.types.is_string_dtype(df[column]):
                # Pick a random existing value
                new_point[column] = random.choice(df[column].dropna().unique())
            else:
                new_point[column] = None
        new_data.append(new_point)
    return pd.DataFrame(new_data)

# Number of additional profiles to generate
num_additional_profiles = 140

# Generate new profiles
df_new = generate_similar_data(df_existing, num_additional_profiles)

# Combine existing and new data
df_combined = pd.concat([df_existing, df_new], ignore_index=True)

# Save to a new Excel file
output_file_path = './profiles_generated_random.xlsx'
df_combined.to_excel(output_file_path, index=False, engine='openpyxl')

print(f"New Excel file saved to: {output_file_path}")
