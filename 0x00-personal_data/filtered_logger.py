#!/usr/bin/env python3

"""
Regex-ing
"""
import re
from typing import List
import logging


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
     a function called filter_datum that returns the log message obfuscated
     """
    regex_pattern = r'({})=([^{}]+)'.format(
            '|'.join(map(re.escape, fields)), separator)
    return re.sub(regex_pattern, r' \1={}'.format(redaction), message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record = logging.Formatter(self.FORMAT).format(record)
        filter = filter_datum(self.fields, self.REDACTION, record,
                              self.SEPARATOR)
        return filter
