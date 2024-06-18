#!/usr/bin/env python3

"""
This code respects the constraints by using super().format
to format the initial message,
then applies filtering using filter_datum
"""

import logging
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str)-> str:
    """
    return the log message
    """
    for field in fields:
        message = re.sub(r'(?<={}=).*?(?={})'.format(field,
                         separator), redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = "; "

    def __init__(self, fields: List[str]):

        """
        Added fields argument to __init__
        constructor and assigned to self.fields.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Implementation of the format method
        that uses super().format(record)
        to get the original message
        and then applies filter_datum
        to filter the specified fields.
        """
        original_message = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION,
                            original_message, self.SEPARATOR)
