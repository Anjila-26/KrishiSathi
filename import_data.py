import os
import sys
import django
import csv
from datetime import datetime
# from django.contrib.auth.decorators import login_required 

# Add the directory containing your settings module to the Python path
sys.path.append(r'C:\Users\anjil\Documents\Code\Farm Management\InventoryManagement\InventoryManagement-Django')

# Manually configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from scraping.models import Vegetables  # Import your model

def import_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Check if the date value is empty or missing
            if not row['date']:
                print("Skipping row with missing date value:", row)
                continue

            try:
                # Attempt to parse the date string and create a datetime object
                date_value = datetime.strptime(row['date'],'%Y-%m-%d').date()
            except ValueError:
                # Handle invalid date format
                print("Invalid date format for row:", row)
                continue

            # Create a new instance of your model for each row in the CSV file
            vegetable = Vegetables(
                product=row['product'],
                date=date_value,
                maximum_price=float(row['max']),
                minimum_price=float(row['min']),
                average_price=float(row['avg'])
            )
            vegetable.save()


if __name__ == '__main__':
    csv_file_path = r'C:\Users\anjil\Documents\Code\Farm Management\InventoryManagement\InventoryManagement-Django\df23.csv'  # Replace with the actual path to your CSV file
    import_data(csv_file_path)



