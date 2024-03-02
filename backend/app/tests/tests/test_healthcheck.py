from app.api.v1.api import schema


def test_healthcheck():
    query = """
    query MyQuery {
        healthcheck {
            status
        }
    }
    """
    health = schema.execute_sync(query)
    print(health)

    assert health.data["healthcheck"]["status"] == 200
