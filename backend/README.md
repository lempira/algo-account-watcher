# Algorand Account Watcher Rest API

The directory contains the REST API backend for the application.

## Tech Used

| Lib or package |             Used for              |
| :------------- | :-------------------------------: |
| Poetry         |      Python package manager       |
| Fast API       |        Rest API Framework         |
| SqlLite        |             Database              |
| Tortoise ORM   | ORM to interact with the database |
| PyTest         |         Testing Framework         |
| Ruff           |              Linting              |
| Ruff           |            Formatting             |
| Docker         |         Container Making          |
| GCP Cloud Run  |            Deployment             |

## Local Development

VsCode was used as the IDE for this development so there are running and debugging tools that are specific to VsCode. The easiest way to develop the API to run Fast API in debug mode using the provided launch configurations shown below. You first have to [open the backend folder in workspace](https://code.visualstudio.com/docs/editor/workspaces#_how-do-i-open-a-vs-code-workspace). You can open the debug extension in vscode (Click [here](https://code.visualstudio.com/docs/python/debugging) for instructions on how to set that up) or press F5. Make sure you are running the "Python Debugger: Algorand Account Watcher API" target. The "Debug Tests" target is for debugging tests.

```
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug Tests",
      "type": "debugpy",
      "request": "launch",
      "module": "pytest",
    },
    {
      "name": "Python Debugger: Algorand Account Watcher API",
      "type": "debugpy",
      "request": "launch",
      "module": "uvicorn",
      "args": ["api.main:app", "--reload"],
      "jinja": true
    }
  ]
}
```

## Linting and Formatting

The backend uses [ruff](https://github.com/astral-sh/ruff) for both linting and formatting. You can run the following command to lint and format the entire codebase. In additionl you should install the [ruff vscode extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) so you can lint and format while working on each file.

```
ruff check # lint
```

```
ruff format
```

## Running Tests

PyTest was used as the Python testing framework. Before running test make sure you are in the correct poetry virtual environment. Activate the virtualenv by running `poetry shell` You can run test by running the following command in the `backend` folder

```
python -m pytest
```

### Test Coverage

You can run test coverate by running `python -m pytest --cov="."` You should get a result like the following

```
---------- coverage: platform linux, python 3.12.3-final-0 -----------
Name                          Stmts   Miss Branch BrPart  Cover
---------------------------------------------------------------
api/__init__.py                   0      0      0      0   100%
api/config.py                    18      0      2      0   100%
api/main.py                      27      0      4      0   100%
api/models/__init__.py            0      0      0      0   100%
api/models/account.py            13      1      0      0    92%
api/models/notification.py       13      1      0      0    92%
api/routes/__init__.py            0      0      0      0   100%
api/routes/addresses.py          33      4     12      3    84%
api/routes/notifications.py      16      1      6      1    91%
api/tasks.py                     35     22      8      0    35%
api/utils.py                     17      0      0      0   100%
---------------------------------------------------------------
TOTAL                           172     29     32      4    81%

```

## Deploy

There are many ways to deploy this application. The include DockerFile creates a repeatable environment image that can be pushed to you cloud platform of choice. I choose to deploy this to Google Cloud [Cloud Run](https://cloud.google.com/run/docs/deploying)

Navigate to the backend directory `algo-account-wathcher/backend` and build the file with the following command:

```
docker build -t <your-api-tag> .
```
