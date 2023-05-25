#!/usr/bin/env python3

"""
Regex-ing
"""
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
     a function called filter_datum that returns the log message obfuscated
     """
    regex_pattern = r'({})=([^{}]+)'.format(
            '|'.join(map(re.escape, fields)), separator)
    return re.sub(regex_pattern, r'\1={}'.format(redaction), message)
