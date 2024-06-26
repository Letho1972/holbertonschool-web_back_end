#!/usr/bin/env python3
""" filter_datum module """
import re
from typing import List
import logging
import mysql.connector
import os


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Constructor """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format the record """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


def filter_datum(
        fields: List[str],
        redaction: str, message: str, separator: str) -> str:
    """
    Filter the message by replacing the words in fields with the redaction
    Args:
        fields: a list of fields to replace in the message
        redaction: a string representing the redacted message
        message: a string representing the log line
        separator: a string representing the separator of fields
    Returns:
        a string representing the log line
    """
    pattern = '|'.join([f"{field}=.*?(?={separator}|$)" for field in fields])
    return re.sub(
        pattern, lambda m: f"{m.group().split('=')[0]}={redaction}", message)


def get_logger() -> logging.Logger:
    """ Get logger function """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Get database connection """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )


def main():
    """ Main function """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    fields = [i[0] for i in cursor.description]

    logger = get_logger()

    for row in cursor:
        message = "; ".join([f"{fields[i]}={row[i]}" for i in range(len(row))])
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
