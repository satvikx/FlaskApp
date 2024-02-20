SQLALCHEMY_DATABASE_URI = 'sqlite:///library.db'

SECRET_KEY = 'MY_SECRET'
# hashes the password and then stores in the database
SECURITY_PASSWORD_SALT = "MY_SECRET"
# allows new registrations to application
SECURITY_REGISTERABLE = True
# to send automatic registration email to user
SECURITY_SEND_REGISTER_EMAIL = False