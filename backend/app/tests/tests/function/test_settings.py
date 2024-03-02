import pytest

from app.core.config import Settings


def test_settings_error():
    with pytest.raises(ValueError):
        Settings(BACKEND_CORS_ORIGINS=123)
