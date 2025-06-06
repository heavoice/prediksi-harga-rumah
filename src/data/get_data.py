# get_data.py
import requests
import pandas as pd

def get_data():
    url = "http://localhost:3000/rumah"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        self = pd.DataFrame(data)
        return self
    else:
        print(f"Error: {response.status_code}")
        return None
