import argparse
from datetime import datetime
import logging
from api_checker import check_api_health
from log_analyzer import analyze_logs
from db_validator import validate_users

logging.basicConfig(
    filename="appwatch_internal.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def generate_report(api_result, log_result, db_result):
    with open("report.txt", "w") as report:
        report.write("APPWATCH MONITORING REPORT\n")
        report.write("="*40 + "\n")
        report.write(f"Generated at: {datetime.now()}\n\n")

        report.write("API HEALTH CHECK\n")
        report.write("-"*40 + "\n")
        report.write(f"Status: {api_result}\n\n")

        report.write("LOG ANALYSIS\n")
        report.write("-"*40 + "\n")
        report.write(f"ERROR Count: {log_result['error_count']}\n")
        report.write(f"WARNING Count: {log_result['warning_count']}\n")
        report.write("Error Details:\n")
        for line in log_result['errors']:
            report.write(f"{line}\n")

        report.write("\nDATABASE VALIDATION\n")
        report.write("-"*40 + "\n")
        report.write(f"Invalid User IDs: {db_result}\n")

def main():
    parser = argparse.ArgumentParser(description="AppWatch Monitoring Tool")
    parser.add_argument("--api", help="API URL to check")
    args = parser.parse_args()

    logging.info("AppWatch execution started")

    api_status = check_api_health(args.api) if args.api else "No API provided"
    log_status = analyze_logs("server.log")
    db_status = validate_users()

    generate_report(api_status, log_status, db_status)

    logging.info("Report generated successfully")
    print("AppWatch Report Generated Successfully!")

if __name__ == "__main__":
    main()
