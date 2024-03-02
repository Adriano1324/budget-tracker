# Budget Tracker bakcend

## Running tests with html report

```bash
docker compose exec web sh -c "coverage run -m pytest; coverage html"
```

## Running linters

```bash
docker compose exec web sh ./scripts/lint.sh  "$@"
docker compose exec web sh ./scripts/format.sh  "$@"
docker compose exec web sh ./scripts/format-imports.sh  "$@"
```