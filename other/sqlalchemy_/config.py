from pydantic import SecretStr, BaseSettings, PostgresDsn


class Config(BaseSettings):
    postgres_dsn_orm: PostgresDsn
    postgres_dsn_sql: PostgresDsn

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = '__'


config: Config = Config()
