from faker import Faker
import csv

def generate_csv_data(
    num_rows: int, filename: str = "small_dataset.csv"
):
    fake = Faker()
    data = []
    for _ in range(num_rows):
        data.append(
            {
                "id": _ + 1,
                "name": fake.name(),
                "email": fake.email(),
                "phone": fake.phone_number(),
                "address": fake.street_address(),
                "city": fake.city(),
                "state": fake.state(),
                "zip": fake.zipcode(),
            }
        )

    with open("./resources/" + filename, "w") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
