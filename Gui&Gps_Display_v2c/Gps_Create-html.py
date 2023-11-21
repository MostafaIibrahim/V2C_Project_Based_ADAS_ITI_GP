import folium
import csv
from time import sleep

csv_file = "gps_reading.csv"
"""
# Read existing GPS readings from CSV file
with open(csv_file, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    # Create a list of coordinates for markers and polyline
    coordinates = [(float(row[0]), float(row[1])) for row in reader]

# Create a map centered around the first GPS reading
m = folium.Map(location=coordinates[0], zoom_start=15)

# Add markers for each GPS reading
for coord in coordinates:
    folium.Marker(location=coord).add_to(m)

# Add a line connecting the GPS readings
folium.PolyLine(locations=coordinates, color='blue').add_to(m)

# Save the map to an HTML file
m.save('gps_map.html')
"""
# Continuously update the map
while True:
    # Read new GPS readings from CSV file
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        new_coordinates = [(float(row[0]), float(row[1])) for row in reader]

    # Update the existing coordinates with new ones
    coordinates = new_coordinates

    # Clear the existing markers and polyline
    m = folium.Map(location=coordinates[0], zoom_start=15)

    # Add markers for each GPS reading
   # for coord in coordinates:
    folium.Marker(location=coordinates[0]).add_to(m)

    # Add a line connecting the GPS readings
    folium.PolyLine(locations=coordinates, color='blue').add_to(m)

    # Save the updated map to an HTML file
    m.save('gps_map.html')
    print("Done")

    # Pause for 1 second before the next update
    sleep(1)

