
# Budget Management Monorepo
This monorepo contains a budget management application that allows users to efficiently manage their finances. 
The application is divided into two main components: the backend, responsible for handling data storage and business logic, and the frontend, providing a user-friendly interface to interact with the budget management system.

Backend
The backend of the application is built using FastAPI. It utilizes Neo4j as the database management system for storing budget-related data. 
Additionally, the backend implements GraphQL for flexible and powerful querying of the budget data.

Technologies Used:
FastAPI
Neo4j
GraphQL

Frontend
The frontend component is developed using Next.js. Apollo Client is used to interact with the GraphQL API provided by the backend, facilitating data fetching and management on the client side.

Technologies Used:
Next.js
Apollo Client
Setup Instructions:

Monorepo Structure
This monorepo follows a structured approach to manage both the backend and frontend components within a single repository. 
Each component resides in its respective directory (backend and frontend), allowing for independent development and testing while sharing common resources and configurations.

graphql

Copy code

## Project structure

```mermaid
budget-tracker/
├── backend                 # Backend directory
│   ├── app                 # Backend source code
│   │   ├── api             # Definition of endpoints
│   │   ├── core            # Singletons etc.
│   │   ├── unions          # Response type unions
│   │   ├── __init__.py
│   │   ├── inputs          # Definitions of inputs for mutations
│   │   ├── main.py
│   │   ├── models          # Neo4j db models
│   │   ├── scalars         # Strawberry types
│   │   ├── security        # Security functionsm context etc.
│   │   └── tests           # Tests
│   ├── Dockerfile          # Backend dockerfile
│   ├── poetry.lock         # Locker versions of packages
│   └── pyproject.toml      # Poetry config
├── docker-compose.yml      # Docker compose file
└── README.md               # (You are here)
```

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request. Make sure to follow the contribution guidelines outlined in the repository.

## License
This project is licensed under the MIT License.

