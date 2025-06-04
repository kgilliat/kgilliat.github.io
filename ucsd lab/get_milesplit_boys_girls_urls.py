import pandas as pd
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

# File path to the CSV
file_path = r"C:\Users\katelorr\Documents\GitHub\UCSD_Lab_1_athletic.net\data\combined_api_responses.csv"

# Function to extract race URLs and text from a single page
def extract_race_urls(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    results_list = soup.find('ul', id='resultFileList')  # Find the <ul> with id 'resultFileList'

    # Extract all <a> tags within the <ul> and their href attributes
    data = []
    if results_list:
        for link in results_list.find_all('a'):
            href = link.get('href')  # Get the href attribute
            text = link.get_text(strip=True)  # Get the text inside the <a> tag
            if href:  # Only include links with an href
                data.append({'race_url': href, 'race': text})
    return data

# Main function to scrape race URLs
def scrape_race_urls(file_path, num_urls=20):
    # Read the CSV file
    urls = pd.read_csv(file_path)
    urls = urls.sort_values(by='year', ascending=False).reset_index(drop=True)

    # DataFrame to store results
    race_urls = pd.DataFrame()

    # Use Playwright to scrape the URLs
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(
            headless=True,
            executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
        )
        page = browser.new_page()

        # Loop through the first `num_urls` URLs in the 'href_url' column
        for url in urls['href_url'][:num_urls]:
            try:
                # Open the webpage
                page.goto(url)

                # Wait for the page to fully load (e.g., wait for a specific element)
                page.wait_for_selector("#content")  # Adjust the selector as needed

                # Scrape the page content
                html_content = page.content()

                # Extract race URLs and text
                data = extract_race_urls(html_content)

                # Append the data to the DataFrame
                if data:
                    race_urls = pd.concat([race_urls, pd.DataFrame(data)], ignore_index=True)
            except Exception as e:
                print(f"Error processing URL {url}: {e}")

        # Close the browser
        browser.close()

    return race_urls

# Run the scraper and save the results
if __name__ == "__main__":
    race_urls_df = scrape_race_urls(file_path, num_urls=50)
    print(race_urls_df)
    # Save the results to a CSV file
    output_file = r"C:\Users\katelorr\Documents\GitHub\UCSD_Lab_1_athletic.net\data\race_urls.csv"
    race_urls_df.to_csv(output_file, index=False)
    print(f"Race URLs saved to {output_file}")