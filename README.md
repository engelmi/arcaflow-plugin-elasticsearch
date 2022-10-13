# Arcaflow Elasticsearch

A plugin for loading data into an Elasticsearch instance.

## Development

During the development of this plugin it is useful to start a local Elasticsearch via:
```bash
docker-compose -f tests/integration/docker-compose.yml up -d
```

and stop it again via:
```bash
docker-compose -f tests/integration/docker-compose.yml down -v
```

## Testing

The tests of this plugin are split up into `unit` and `integration` tests located in 
- [./tests/integration/](./tests/integration/)
- [./tests/unit/](./tests/unit/)

Run them via:
```bash
# Run all unit tests
python -m unittest tests.unit.test_es_plugin

# Run all integration tests
python -m unittest tests.integration.test_es_plugin
```

Prerequisite: For running the `integration` tests locally, an Elasticsearch instance is required. Start one as described in [Development](#development)