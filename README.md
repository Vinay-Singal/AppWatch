# AppWatch – Application Monitoring & Validation Tool

AppWatch is a Python-based monitoring tool designed for Application Support Engineers.

## Features

- API Health Check
- Log File Analysis
- MongoDB Data Validation
- Automated Report Generation
- CLI Support
- Internal Logging

## Setup

Install dependencies:

pip install -r requirements.txt

Ensure MongoDB is running locally.

Database: appwatch_db  
Collection: users

## Run

Check API health:

python main.py --api https://URL

Run without API:

python main.py

## Output

- report.txt → Monitoring report
- appwatch_internal.log → Internal logs
