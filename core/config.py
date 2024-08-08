from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    db_url: str = "sqlite+aiosqilte:///./db/sqilte3"
    db_echo: bool = True


settings = Setting()
