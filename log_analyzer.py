import logging

def analyze_logs(file_path):
    error_count = 0
    warning_count = 0
    errors = []

    try:
        with open(file_path, "r") as file:
            for line in file:
                if "ERROR" in line:
                    error_count += 1
                    errors.append(line.strip())
                elif "WARNING" in line:
                    warning_count += 1

        logging.info("Log analysis completed")

        return {
            "error_count": error_count,
            "warning_count": warning_count,
            "errors": errors
        }

    except FileNotFoundError:
        logging.error("Log file not found")
        return {
            "error_count": 0,
            "warning_count": 0,
            "errors": ["Log file not found"]
        }
