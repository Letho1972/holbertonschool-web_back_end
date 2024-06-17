#!/usr/bin/env python3

"""
0. Regex-ing
Write a function called filter_datum
that returns the log message obfuscated

"""

import re

from typing import List, Union


def filter_datum(fields: list[str], redaction: str,
                 message: Union[str, List[str]], separator: str):
    """
    Returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(f"{field}{separator}[^{separator}]*",
                         f"{field}{separator}{redaction}", message)

    return message
