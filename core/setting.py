import os
from pydantic import BaseSettings


class Setting(BaseSettings):
    NAME: str
    DATABASE_URL: str
    JWT_KEY: str
    JWT_ISSUER: str
    JWT_AUDIENCE: str
    JWT_ALGORITHM: str

    class Config:
        envName = os.getenv('ENVIRONMENT', 'dev')
        filename = f'{envName}.env'
        env_file = filename


setting = Setting()
