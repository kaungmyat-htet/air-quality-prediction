import json
import pandas as pd
from datetime import datetime

def json_to_csv(json_file, output_file):
    print(json_file)
    with open(json_file) as file:
        data = json.load(file)
        
    coordinates = data['coord']
    lon, lat = coordinates['lon'], coordinates['lat']
    
    csv_data = []
    
    for item in data['list']:
        row = {
            'date': datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d'),
            'time': datetime.fromtimestamp(item['dt']).strftime('%H:%M:%S'),
            'longitude': lon,
            'latitude': lat,
            'aqi': item['main']['aqi'],
            'co': item['components']['co'],
            'no': item['components']['no'],
            'no2': item['components']['no2'],
            'so2': item['components']['so2'],
            'o3': item['components']['o3'],
            'pm2_5': item['components']['pm2_5'],
            'pm10': item['components']['pm10'],
            'nh3': item['components']['nh3']
        }
        csv_data.append(row)
        
    df = pd.DataFrame(csv_data)
    
    print(df.head(5))
    # pollution_df = pd.json_normalize(data['list'])
    # print(pollution_df.head(5))
    df.to_csv(output_file, index=False)
    print(f"CSV file {output_file} has been created successfully.")
