from pydantic import Field
from pydantic import ValidationError
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ib_host: str = Field(default="127.0.0.1", env="IB_DEFAULT_HOST")
    ib_client_id: int = Field(default=1, env="IB_CLIENT_ID")
    ib_port: int = Field(default=7497, env="IB_DEFAULT_PORT")
    is_live_trading: bool = Field(default=False, env="IS_LIVE_TRADING")

    def __init__(self, **data):
        super().__init__(**data)

        if self.is_live_trading:
            raise ValueError(
                "Live trading is not supported yet"
            )  ## todo: implement live trading by uncommenting next line
            # self.ib_default_host = 7496


try:
    settings = Settings()
except ValidationError as e:
    print(f"Configuration error: {e}")
    raise
