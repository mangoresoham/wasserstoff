import json
import requests
import urllib.parse

# Load the JSON file
json_file = 'D:\\Programming\\Projects\\WASSERSTOFF\\Data\\Dataset.json'
failed_downloads_file = 'failed_downloads.txt'

# Open the JSON file
with open(json_file, 'r') as f:
    data = json.load(f)

# Headers to simulate a real browser request (useful for some sites)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Initialize a counter for naming the files
pdf_counter = 1

# Loop through the dictionary and download each PDF
for pdf_name, pdf_url in data.items():
    try:
        print(f"Downloading {pdf_name} from {pdf_url}...")
        
        # Create a new file name using the iterative numbering scheme
        output_filename = f"pdf{pdf_counter}.pdf"
        
        # Send GET request to download the file
        response = requests.get(pdf_url, headers=headers, stream=True, allow_redirects=True, timeout=15)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Save the file locally with the unique name
            with open(output_filename, 'wb') as pdf_file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:  # Filter out keep-alive chunks
                        pdf_file.write(chunk)
            print(f"{output_filename} downloaded successfully.")
            
            # Increment the counter for the next file
            pdf_counter += 1
        else:
            raise Exception(f"Failed to download {pdf_url}. HTTP Status: {response.status_code}")

    except Exception as e:
        # If there is any exception, write the URL and error to a failure log
        print(f"Error downloading {pdf_name}: {e}")
        with open(failed_downloads_file, 'a') as f:
            f.write(f"Failed to download: {pdf_url} | Error: {e}\n")
        continue

print("Download process completed.")
