from passlib.context import CryptContext

# make object of CryptContext class
pwt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher():
    # so you don't have to create a new object everytime you want to hash a password
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwt_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(plain_password):
        return pwt_context.hash(plain_password)