import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Define the parameters and root URL
params = {
    'years': list(range(2012, 2025)),
    'months': list(range(8, 13)),
    'seasons': ['outdoor'],
    'level': ['hs']
}

root_url = "https://ca.milesplit.com/results/?"

# Generate the URLs
urls = [
    f"{root_url}year={year}&month={month}&season={season}&level={level}"
    for year in params['years']
    for month in params['months']
    for season in params['seasons']
    for level in params['level']
]

# Function to make GET requests with pagination and extract data
def fetch_data(url):
    page = 1
    data = []
    while True:
        paginated_url = f"{url}&page={page}"
        response = requests.get(paginated_url, verify=False)
        if response.status_code != 200:
            break
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table')
        if not table:
            print(f"No table found for URL: {paginated_url}")
            break
        # Check if the table has content
        rows = table.find_all('tr')
        if not rows:
            print(f"Table found but it has no content for URL: {paginated_url}")
            break
        # Extract table data
        for row in rows:
            cells = row.find_all('td')
            row_data = [cell.text.strip() for cell in cells]
            # Extract the href URL from the name element
            name_element = row.find('td', class_='name')
            if name_element:
                a_tag = name_element.find('a')
                href_url = a_tag['href'] if a_tag else None
            else:
                href_url = None
            row_data.append(href_url)
            data.append({"url": paginated_url, "row_data": row_data})
        page += 1
    return data

# Initialize a list to store the data
all_data = []

# Make GET requests for each URL
for url in urls[0:1]:
    all_data.extend(fetch_data(url))

# Create a DataFrame from the collected data
df = pd.DataFrame(all_data)

# Extract additional columns from the URL
df['year'] = df['url'].str.extract(r'year=(\d+)')
df['month'] = df['url'].str.extract(r'month=(\d+)')
df['season'] = df['url'].str.extract(r'season=(\w+)')
df['level'] = df['url'].str.extract(r'level=(\w+)')
df['page'] = df['url'].str.extract(r'page=(\d+)')

# Ensure the "data" folder exists
os.makedirs("data", exist_ok=True)

# Save the DataFrame to a CSV file in the "data" folder
csv_path = os.path.join("data", "api_responses_with_tables.csv")
df.to_csv(csv_path, index=False)

print(f"Data saved to {csv_path}")