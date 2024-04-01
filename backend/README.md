# Budget Tracker bakcend

## Important links
- GraphQL playground: `http://127.0.0.1:8000/api/v1/graphql`
- Neo4j browser: `http://127.0.0.1:7474/`
    - username: `neo4j`
    - password: `testtest`


## Running tests with html report

```bash
docker compose exec web sh -c "coverage run -m pytest; coverage html"
```

## Running linters

```bash
docker compose exec web sh ./scripts/lint.sh "$@"
docker compose exec web sh ./scripts/format.sh "$@"
docker compose exec web sh ./scripts/format-imports.sh "$@"
```

## Applying and removing constraints and indexes

All following commands must be executed inside of web constainer

```sh
docker compose exec web sh  # To get web container console
```

### Applying constraints and indexes

```sh
neomodel_install_labels app/main.py app.models --db bolt://neo4j:testtest@db:7687
```

### Remove existing constraints and indexes

```sh
neomodel_remove_labels --db bolt://neo4j:testtest@db:7687
```