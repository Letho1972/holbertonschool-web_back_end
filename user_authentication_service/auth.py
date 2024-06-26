import bcrypt


def _hash_password(password: str) -> bytes:
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the generated salt
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password
