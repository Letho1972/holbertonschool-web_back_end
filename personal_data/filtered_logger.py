#!/usr/bin/env python3

"""
0. Regex-ing
Write a function called filter_datum
that returns the log message obfuscated

"""

import re
from typing import List


def filter_datum(fields: list[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns the log message obfuscated """

    return re.sub(f'({"|".join(fields)})=[^{separator}]*',
                  lambda match: match.group(0).split('=')[0] + f'={redaction}',
                  message)
