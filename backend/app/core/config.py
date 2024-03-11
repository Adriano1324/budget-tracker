"""
This module is creating settings object
"""

from typing import List, Union

from neomodel import config
from pydantic import field_validator  # pylint: disable=E0611
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    This is class which store our configuration
    """

    API_V1_STR: str = "/api/v1"
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str = "localhost"
    SERVER_HOST: str = "http://localhost"
    BACKEND_CORS_ORIGINS: Union[str, List[str]] = ["*"]

    NEO4J_CONN_STRING: str = ""

    @field_validator("NEO4J_CONN_STRING", mode="before")
    def set_neo4j_config(  # noqa E501 pylint: disable=E0213
        cls, v: str
    ) -> str:  # noqa E501 pylint: disable=E0213
        config.DATABASE_URL = v  # default
        return v

    PROJECT_NAME: str = "budget tracker"

    class Config:  # pylint: disable=R0903
        """
        This class is setting that our settings are case_sensitive
        """

        case_sensitive = True


settings = Settings()
