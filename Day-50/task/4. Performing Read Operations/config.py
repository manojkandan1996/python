import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URI", "sqlite:///dev.db")
    DEBUG = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("PROD_DATABASE_URI")
    DEBUG = False


# Choose config based on ENV variable
config_by_name = {
    'development': DevConfig,
    'production': ProdConfig
}
