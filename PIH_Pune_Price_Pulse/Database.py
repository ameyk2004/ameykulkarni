import csv
import os
area_data = []
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the CSV file
csv_file_path = os.path.join(current_dir, 'Data', 'HTML data', 'area data.csv')

# Read data from the CSV file
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        # Extract data from the row

        area_name = row[0]
        image = row[1]
        avg_sell_price = row[2]
        house_price = row[3]
        avg_rent_price = row[4]

        if row[0] != 'Area Name':
            area_data.append(row)


