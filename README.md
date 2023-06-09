# gb-api-tests

*Work In Progress*

This repository contains API tests for [GameBanana](https://gamebanana.com)

Target API version: `11`

## Basic concepts and terms

GameBanana (GB) is the game modding community established in 2001.

Submission (Mod) is a piece of work uploaded to the website.

Model (Record) is a submission of a specific type.

Currently, GB is *partially* APIfied (see gb-api-v11 on [GitHub](https://github.com/s0nought/gb-api-v11) or [Postman](https://www.postman.com/s0nought/workspace/gb-api-v11)).

Being a member of the Dev-Tester team at GameBanana I would like to automate some basic checks and crontab them.

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

### tests_data/credentials.py.example

Fill in your login and password.

Rename `credentials.py.example` to `credentials.py`.

### Visual Studio Code

`.vscode/settings.json`

```
{
    "python.analysis.extraPaths": [
        "./endpoints",
        "./tests_data"
    ]
}
```

## Run tests

```
cd ~/gb-api-tests && pytest
```
