"""
This module is responsible for registering all routers
"""

import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig

from app.scalars import HealthcheckStatus


@strawberry.type
class Query:
    """
    This is base query class which inherits from all modules
    """

    @strawberry.field
    def healthcheck(self) -> HealthcheckStatus:
        return HealthcheckStatus(status=200)


@strawberry.type
class Mutation:  # pylint: disable=R0903
    """
    This is base mutation class which inherits from all modules
    """

    @strawberry.mutation
    def dummy_mutation(self, text: str) -> str:
        return text


schema = strawberry.Schema(
    query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=True)
)

api_router_v1: GraphQLRouter = GraphQLRouter(schema, path="/graphql")
