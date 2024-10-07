import bcrypt
import logging

logging.basicConfig(level=logging.INFO)

def hash_password(password):
    logging.info('Hashing password')
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed):
    logging.info('Check password')
    return bcrypt.checkpw(password.encode('utf-8'), hashed)
