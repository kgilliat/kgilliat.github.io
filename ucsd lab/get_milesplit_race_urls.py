import pandas as pd
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

meets_url_file_path = r"C:\Users\katelorr\Documents\GitHub\UCSD_Lab_1_athletic.net\data\combined_api_responses.csv"

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

# Main function to scrape race URLs and save results by year
def scrape_race_urls_by_year(file_path, year_cutoff):
    # Read the CSV file
    urls = pd.read_csv(file_path)
    urls = urls.sort_values(by='year', ascending=False).reset_index(drop=True)
    urls = urls[urls['year']>=year_cutoff]

    # DataFrame to store errors
    errors = pd.DataFrame(columns=['race_url', 'error'])

    # Use Playwright to scrape the URLs
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(
            headless=True,
            executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
        )
        page = browser.new_page()

        # Loop through the URLs grouped by year
        for year, group in urls.groupby('year'):
            print(f"Processing year: {year}")
            results = pd.DataFrame()

            for index, row in group.iterrows():
                url = row['href_url']
                print(f"Processing URL: {url}")
                try:
                    # Open the webpage
                    page.goto(url)

                    # Wait for the page to fully load (e.g., wait for a specific element)
                    page.wait_for_selector("#content")  # Adjust the selector as needed

                    # Scrape the page content
                    html_content = page.content()

                    # Extract race URLs and text
                    data = extract_race_urls(html_content)

                    # Append the data to the results DataFrame for the current year
                    if data:
                        print("Extracted data")
                        results = pd.concat([results, pd.DataFrame(data)], ignore_index=True)
                except Exception as e:
                    # Log the error and the URL to the errors DataFrame
                    errors = pd.concat([errors, pd.DataFrame({"race_url": [url], "error": [str(e)]})], ignore_index=True)

            # Save the results for the current year to an Excel file
            output_file = rf"C:\Users\katelorr\Documents\GitHub\UCSD_Lab_1_athletic.net\data\race_urls_{year}.csv"
            results.to_csv(output_file, index=False)
            number_of_results = len(results)
            print(f"{number_of_results} results for year {year} saved to {output_file}")

        # Close the browser
        browser.close()

    # Save errors to a separate Excel file
    errors_file = r"C:\Users\katelorr\Documents\GitHub\UCSD_Lab_1_athletic.net\data\errors.csv"
    errors.to_csv(errors_file, index=False)
    print(f"Errors saved to {errors_file}")

# Run the scraper
if __name__ == "__main__":
    scrape_race_urls_by_year(meets_url_file_path, year_cutoff=2010)