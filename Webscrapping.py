import requests
from bs4 import BeautifulSoup
import csv
import os

data_path = r'D:\INTERNSHIP'

def scrape_url(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all the paragraph and heading texts
            paragraphs = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

            # Create a list to store the scraped data
            data = []

            # Loop through the paragraphs and extract the text
            for paragraph in paragraphs:
                data.append(paragraph.text.strip())

            return data
        else:
            print("Failed to retrieve the webpage")
            return None
    except Exception as e:
        print("An error occurred: ", str(e))
        return None

def save_to_csv(data, filename):
    try:
        # Ensure the data_path directory exists
        os.makedirs(data_path, exist_ok=True)

        # Full path for the csv file
        full_path = os.path.join(data_path, filename)

        # Create a CSV file and write the data to it
        with open(full_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Data"])  # header row
            for item in data:
                writer.writerow([item])
        print("Data scraped and saved to", full_path)
    except Exception as e:
        print("An error occurred while saving to CSV:", str(e))

def main():
    url = input("Enter the URL to scrape: ")
    filename = input("Enter the filename to save (default: output.csv): ")
    if filename.strip() == "":
        filename = "output.csv"
    if not filename.endswith(".csv"):
        filename += ".csv"

    data = scrape_url(url)
    if data is not None:
        save_to_csv(data, filename)

if __name__ == "__main__":
    main()
