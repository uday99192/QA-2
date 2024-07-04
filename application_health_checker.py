import requests
import logging

# Set up logging
logging.basicConfig(filename="application_health.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Application URL
APPLICATION_URL = "http://example.com"  # Replace with the actual application URL

def check_application_health():
    try:
        response = requests.get(APPLICATION_URL, timeout=5)
        if response.status_code == 200:
            logging.info(f"Application is up. Status code: {response.status_code}")
        else:
            logging.warning(f"Application is down. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Application is down. Error: {e}")

if __name__ == "__main__":
    check_application_health()
