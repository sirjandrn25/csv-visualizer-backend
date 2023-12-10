
import bcrypt
salt_key = '10'
def make_hash(password):
    hashed_password = bcrypt.hashpw(password, salt_key)
    return hashed_password
def check_pass(password:str, hashed_password:str):
    if bcrypt.checkpw(password, hashed_password):
        return True
    else:
        return False