# gb-api-tests

*Work In Progress*

This repository contains API tests for [GameBanana](https://gamebanana.com)

Target API version: `11`

## Installation

1. Clone this repository to a local directory
    ```
    git clone https://github.com/s0nought/gb-api-tests.git ~/gb-api-tests
    ```

1. Install required Python modules
    ```
    cd ~/gb-api-tests
    pip install -r requirements.txt
    ```

## Configuration

### src/modules/credentials.py.example

Fill in your login and password.

Rename `credentials.py.example` to `credentials.py`.

## Run tests

```
cd ~/gb-api-tests/src
pytest
```

## Tests

- Add Thread
