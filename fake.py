import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta


# Initialize Faker
fake = Faker()

# Function to generate random profit or loss
def generate_profit():
    return round(random.uniform(-50, 2000), 2)  # Generate random float between -50 and 2000

# Create an empty list to store the data
data = []
start_datetime = datetime(2015, 1, 1, 0, 0)

# Generate 1000 entries
for i in range(1, 510001):
    row = {
        "Sl.No": i,
        "Date": start_datetime + timedelta(minutes=30 * (i - 1)),
        "Clothing": generate_profit(),
        "Food": generate_profit(),
        "Home-decor": generate_profit(),
        "Electronics": generate_profit(),
        "Stationary": generate_profit(),
    }
    data.append(row)

# Convert the list of dictionaries into a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("fake_data_table.csv", index=False)

print("Table with 1000 entries of fake data has been created and saved as 'fake_data_table.csv'.")
