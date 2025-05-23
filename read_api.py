import csv
import requests  # Ensure requests library is installed

# ThingSpeak Channel Details
api_key = 'RGQQBAZPUN7PSDAK'  # Replace with your ThingSpeak Write API Key
channel_url = 'https://api.thingspeak.com/update'

# Input CSV File
input_file = "C:/research paper/serial_monitor_export.csv"  # Replace with your CSV file name

# Extract and Upload Temperature Data
with open(input_file, "r") as infile:
    reader = csv.reader(infile)
    for row in reader:
        for cell in row:
            try:
                # Attempt to parse the cell as a float (temperature value)
                temperature = float(cell)  # Convert to float to ensure it's a number
                
                # Upload to ThingSpeak
                data = {
                    'api_key': api_key,
                    'field1': temperature,  # Use the extracted temperature
                }
                response = requests.post(channel_url, data=data)
                if response.status_code == 200:
                    print(f"Uploaded Temperature: {temperature}")
                else:
                    print(f"Failed to upload Temperature: {temperature}, Status Code: {response.status_code}")
            except ValueError:
                # Skip cells that are not numeric
                pass
