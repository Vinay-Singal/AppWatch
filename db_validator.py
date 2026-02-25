from pymongo import MongoClient
import logging

def validate_users():
    invalid_users = []

    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["appwatch_db"]
        collection = db["users"]

        users = collection.find()

        for user in users:
            if "email" not in user:
                invalid_users.append(str(user["_id"]))

        logging.info("Database validation completed")

        return invalid_users

    except Exception as e:
        logging.error(f"Database validation failed: {str(e)}")
        return [f"DB Error: {str(e)}"]
