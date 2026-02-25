import requests
from datetime import datetime
import logging

def check_api_health(url):
    if not url:
        return "No URL Provided"

    try:
        response = requests.get(url, timeout=5)
        status = response.status_code
        timestamp = datetime.now()

        logging.info(f"API checked: {url} - Status: {status}")

        return f"URL: {url}, Status Code: {status}, Checked At: {timestamp}"

    except requests.exceptions.RequestException as e:
        logging.error(f"API check failed: {str(e)}")
        return f"API Check Failed: {str(e)}"
