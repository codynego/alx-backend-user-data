#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Returns a salted, hashed password as byte string
    """
    encode = password.encode()
    hashe = bcrypt.hashpw(encode, bcrypt.gensalt())

    return hashe


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate the password matches the hashed password
    """
    isvalid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        isvalid = True
    return isvalid
