import requests
import time
import threading
import random

"""
sitepulse.py: A simple script to visit websites at regular intervals.
- Free tier server services often require periodic visits to keep them active.
- When such services are not visited for a certain period, you may be unable to visit your hosted sites.
- Prolong the time-to-live of server services by keeping them active, even when you're not using them.
- Thereby keeping your website alive and accessible to everyone.

Usage:
- Run the script in the terminal and provide the number of websites you want to visit.
- Enter the address of each website and the interval (in minutes) at which you want to visit it.
- Run it either on you main computer, or like I do, on a seperate Raspberry Pi.

Have been tested and known to work on:
- render.com
- supabase.com
"""


# Function to visit a website at a given interval
def visit_website(url, base_interval):
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Successfully visited {url}")
            else:
                print(f"Received unexpected status code {response.status_code} from {url}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while trying to visit {url}: {e}")

        # Generate a random interval around the base interval
        random_interval = random.uniform(base_interval * 0.8, base_interval * 1.2)
        print(f"Next visit to {url} in {random_interval / 60:.2f} minutes")
        time.sleep(random_interval)

# Main function with arrays of websites and intervals based on user input
def main():
    websites = []
    base_intervals = []

    num_sites = int(input("How many websites should I visit? "))

    for i in range(num_sites):
        url = input(f"What is the address of the {i + 1} website? ")
        base_interval = int(input(f"At what interval (in minutes) should I visit {url}? ")) * 60
        websites.append(url)
        base_intervals.append(base_interval)

    # Start a thread for each website
    for i in range(num_sites):
        thread = threading.Thread(target=visit_website, args=(websites[i], base_intervals[i]))
        thread.daemon = True  # Daemon threads will exit when the main program exits
        thread.start()

    # Keep the main thread alive
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
