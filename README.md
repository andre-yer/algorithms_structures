# Algorithms & structures

## SET UP (Visual Studio Code)

### Windows
For setting up this project first of all open it in main folder `~/algorithms_structures`. Then go to `Settings->settings.json` and add those lines:
```json
{
    "python.linting.pylintArgs": [
        "--init-hook='import sys; sys.path.append(\"path_to_project\\algorithms_structures\")'"
    ],
    "terminal.integrated.env.windows": {
        "PYTHONPATH": "path_to_project\\algorithms_structures"
    },
}
```
For example, my json file is:
```json
{
    "python.linting.pylintArgs": [
        "--init-hook='import sys; sys.path.append(\"c:\\Users\\Andrey\\algorithms_structures\")'"
    ],
    "terminal.integrated.env.windows": {
        "PYTHONPATH": "c:\\Users\\Andrey\\algorithms_structures"
    },
}
```
To activate unittest go to `.vscode->setting.json` and set up it like this:
```json
{
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./tests",
        "-p",
        "*_test.py"
    ],
    "python.testing.pytestEnabled": false,
    "python.testing.nosetestsEnabled": false,
    "python.testing.unittestEnabled": true
}
```