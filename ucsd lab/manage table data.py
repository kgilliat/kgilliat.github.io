
"""
# Main function to scrape race URLs and save results by year
def scrape_race_results_by_year(file_path, num_urls=5, first_year = 2022):
    # Read the CSV file
    urls = pd.read_csv(file_path)
    urls = urls.sort_values(by='year', ascending=False).reset_index(drop=True)
    urls = urls[urls['year']>=first_year]

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
            results = {
                'individual': pd.DataFrame(),
                'team': pd.DataFrame()
            }

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
                    data_tables = extract_table_data(html_content)

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
    scrape_race_urls_by_year(meets_url_file_path, num_urls=5)

        data = []

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
    return data


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


session = HTMLSession()
r = session.get(url, verify=False)
r.html.render(timeout=60)
print(r.html.text)

page = requests.get(url, cookies=cookies_dict, verify = False)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.text)
"""