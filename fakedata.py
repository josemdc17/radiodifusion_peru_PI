import csv
from faker import Faker

fake = Faker()

# Generate 3000 rows of fake data
data = []
for _ in range(10000):
    row = [
        fake.uuid4(),            # id
        fake.first_name(),
        fake.last_name(),        # surname
        fake.last_name(),        # lastname
        fake.random_int(18, 80),  # age
        fake.random_element(["Married", "Single"])  # married or single
    ]
    data.append(row)

# Write the data to a CSV file
csv_filename = "mock_data.csv"
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(["id", "first name", "surname", "lastname", "age", "married or single"])
    # Write data rows
    writer.writerows(data)

print(f"Mock data has been generated and saved to {csv_filename}.")
