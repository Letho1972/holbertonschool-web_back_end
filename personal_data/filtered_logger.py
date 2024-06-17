#!/usr/bin/env python3

"""
0. Regex-ing
Write a function called filter_datum
that returns the log message obfuscated

"""
import logging
import re


def filter_datum(fields, redaction, message, separator):

    for field in fields:
        message = re.sub(f"{field}{separator}[^{separator}]*",
                         f"{field}{separator}{redaction}", message)

    return message
