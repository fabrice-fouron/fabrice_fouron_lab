# Lab 7
## Setup
Things to install: python, MySQL server on docker or on the machine itself

- For python, create an environment from which you will run the code. Install the following packages: ```uvicorn```, ```fastapi```, ```requests```

- For the MySQL server, make sure that the database ```my_guitar_shop``` is already populated

## How to run
First, you need to open the terminal in the **LAB7/** folder.

To run the server, you enter:
```
uvicorn main:app --port 8080
```

Next, you will need to run the cli driver by entering this in a different terminal, and in the same **LAB7/** directory:
```
python cli_driver.py
```

Follow the CLI's directions to use it.
