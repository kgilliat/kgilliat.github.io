import re
import pandas as pd
import get_milesplit_formatted_meet_results as milesplit_results
import glob
import os

# Function to extract the meet ID from the URL
def extract_meet_id(url):
    match = re.search(r'meets/(\d+)-', url)
    return match.group(1) if match else url

# Function to extract the year from the file path
def extract_meet_year(file_path):
    match = re.search(r'_(\d{4})', file_path)
    return match.group(1) if match else None

# Function to process URLs grouped by meet ID and save results
def process_meets_and_save(urls_by_meet_id, output_dir):
    os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists
    all_metadata_results = pd.DataFrame()
    error_log_file = os.path.join(output_dir, "error_log.txt")

    for meet_id, urls in urls_by_meet_id.items():
        print(f"Processing meet ID: {meet_id} with {len(urls)} races")

        try:
            individual_results, team_results, metadata_results = milesplit_results.process_urls_and_save(urls)

            if not metadata_results.empty:
                metadata_results['meet_id'] = meet_id
                all_metadata_results = pd.concat([all_metadata_results, metadata_results], ignore_index=True)

            # Save the combined results for the current meet
            save_meet_results(meet_id, individual_results, team_results, output_dir)
        except Exception as e:
            #Log error to error text file
            with open(error_log_file, 'a') as error_file:
                error_file.write(f"Error processing meet ID {meet_id}: {e}\n")
            print(f"Error processing meet ID {meet_id}: {e}")

    return all_metadata_results

# Function to save individual and team results for a meet
def save_meet_results(meet_id, individual_results, team_results, year_output_dir):
    individual_results_file = os.path.join(year_output_dir, f"individual_results_meet_{meet_id}.csv")
    team_results_file = os.path.join(year_output_dir, f"team_results_meet_{meet_id}.csv")

    if not individual_results.empty:
        individual_results.to_csv(individual_results_file, index=False)
        print(f"Saved individual results for meet ID {meet_id} to {individual_results_file}")

    if not team_results.empty:
        team_results.to_csv(team_results_file, index=False)
        print(f"Saved team results for meet ID {meet_id} to {team_results_file}")

# Main function to process all files and save metadata
def main():
    file_paths = glob.glob("data/race_urls_*.csv")

    all_metadata_results = pd.DataFrame()

    for file in file_paths:
        year = extract_meet_year(file)
        year_output_dir = os.path.join("output", year)
        os.makedirs(year_output_dir, exist_ok=True)  # Ensure the output directory exists
        
        print(f"Processing file: {file} with year: {year}")
        df = pd.read_csv(file)
        df['year'] = extract_meet_year(file)
        df['meet_id'] = df['race_url'].apply(extract_meet_id)

        urls_by_meet_id = df.groupby('meet_id')['race_url'].apply(list).to_dict()
        print(f"Processing {len(urls_by_meet_id)} meet IDs from file: {file}")

        # Process the URLs and save results
        try:
            metadata_results = process_meets_and_save(urls_by_meet_id, output_dir = year_output_dir)
            all_metadata_results = pd.concat([all_metadata_results, metadata_results], ignore_index=True)
            # Save metadata for all meets processed
            metadata_file = os.path.join("output", "metadata_results.csv")
            all_metadata_results.to_csv(metadata_file, index=False)
            print(f"Saved metadata results to {metadata_file}")
        except Exception as e:
            print(f"Error processing file {file}: {e}")
            with open(os.path.join(year_output_dir, "error_log.txt"), 'a') as error_file:
                error_file.write(f"Error processing file {file}: {e}\n")
        

# Run the script
if __name__ == "__main__":
    main()