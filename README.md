# dses-if-ws
Webserver interface for the DSES Interferometer controller.

## Usage
See [Makefile](./Makefile) for all targets, or call `make help`.

### Running the webserver
```bash
$ make run
```

With debug output:

```bash
$ make run.debug
```

### Dependency Management
Install project dependencies into Poetry's virtual environment.

```bash
$ poetry install
```

### Formatting and Linting
Format and lint the source code.

```bash
$ make format lint
```
