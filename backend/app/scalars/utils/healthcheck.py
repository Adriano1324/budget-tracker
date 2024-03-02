import strawberry


@strawberry.type
class HealthcheckStatus:
    status: int
