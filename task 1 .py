import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_data():
    # Fetching data for countries in the Americas
    response = requests.get("https://restcountries.com/v3.1/region/americas")
    if response.status_code == 200:
        data = response.json()
        rows = []
        for country in data:
            rows.append({
                "Name": country.get('name', {}).get('common'),
                "Population": country.get('population', 0),
                "Area": country.get('area', 0)
            })
        return pd.DataFrame(rows)

def visualize(df):
    # Top 10 by population
    top_10 = df.nlargest(10, 'Population')
    
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_10, x='Population', y='Name', palette='mako')
    plt.title('Top 10 Most Populous Countries in the Americas')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = get_data()
    if df is not None:
        visualize(df)
