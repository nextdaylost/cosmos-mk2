# Cosmos

A system for processing, storing, and sharing data.

## Development

### Prerequisites

- [Python 3.11](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/)

### Setup

Create an isolated environment for development:

```shell
poetry env use </path/to/python/interpreter>
```

Install the project in edit mode for development:

```shell
poetry install --with dev
```

Open an interactive shell session in the development environment:

```shell
poetry shell
```

> **Note**: All commands which rely on installed packages will assume that you are
> working from an interactive shell session. If you are not, you will need to
> prefix those commands with `poetry run`.

### Testing

Run the test suite:

```shell
pytest
```

Gather code coverage information:

```shell
coverage run -m pytest
```

Generate a coverage report:

```shell
# Printing to STDOUT
coverage report

# As browsable HTML
coverage html

# As machine-readable XML
coverage xml
```

### Linting

Run the linter:

```shell
flake8
```

> Code formatting errors can usually be fixed by running `black`:
>
> ```shell
> black src/cosmos/
> ```
