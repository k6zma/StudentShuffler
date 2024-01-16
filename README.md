# Student Shuffler Telegram Bot

<div align="center">
<img src="https://img.shields.io/badge/PYTHON-black?style=for-the-badge&logo=python&logoColor=gold"/><img src="https://img.shields.io/badge/TELEGRAM-black?style=for-the-badge&logo=telegram&logoColor="/><img src="https://img.shields.io/badge/LINUX-black?style=for-the-badge&logo=linux&logoColor="/><img src="https://img.shields.io/badge/DOCKER-black?style=for-the-badge&logo=Docker&logoColor=blue"/><img src="https://img.shields.io/badge/GIT-black?style=for-the-badge&logo=git&logoColor=orange"/><img src="https://img.shields.io/badge/GITHUB-black?style=for-the-badge&logo=GitHub&logoColor=white"/><img src="https://img.shields.io/badge/VSC-black?style=for-the-badge&logo=Visual Studio Code&logoColor=007ACC"/>
</div>


<p></p>
<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
![GitHub Issues](https://img.shields.io/github/issues/k6zma/StudentShuffler.svg)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/k6zma/StudentShuffler.svg)
![Stars](https://img.shields.io/github/stars/k6zma/StudentShuffler.svg)

</div>

<div align="center">
  
<img src="img/group_logo.jpg" alt="logo">

</div>

## Link to a chat with a bot (it’s best to add this bot to a chat or group): <a>https://t.me/m3112_is_bot</a>

## This Telegram bot is created for IS students from M3112 group. It helps you automatically create the order in which different jobs are due.

## Peculiarities
- Random mixing of students;
- Opportunity to mark yourself as ready for delivery;
- Simple and intuitive interface.

## Project structure:
```
StudentShuffler
├── Dockerfile
├── README.md
├── docker-compose.yaml
├── img
│   └── group_logo.jpg
├── requirements.txt
└── src
    ├── bot
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-39.pyc
    │   │   └── keyboards.cpython-39.pyc
    │   ├── handlers
    │   │   ├── admin_side
    │   │   │   ├── __init__.py
    │   │   │   ├── __pycache__
    │   │   │   │   ├── __init__.cpython-39.pyc
    │   │   │   │   └── handlers.cpython-39.pyc
    │   │   │   └── handlers.py
    │   │   └── user_side
    │   │       ├── __init__.py
    │   │       ├── __pycache__
    │   │       │   ├── __init__.cpython-39.pyc
    │   │       │   └── handlers.cpython-39.pyc
    │   │       └── handlers.py
    │   └── keyboards.py
    ├── config
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-39.pyc
    │   │   └── settings.cpython-39.pyc
    │   └── settings.py
    ├── database
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-39.pyc
    │   │   └── db_generating.cpython-39.pyc
    │   └── db_generating.py
    └── main.py
```

## Installation and launch:
1. First of all, you need to copy the repository from <b>`GitHub`</b>:
    ```bash
    git clone https://github.com/k6zma/StudentShuffler.git
    ```
2. Setting up data for a group (API key to access the bot, names of classmates, names of classmates and their telegram tags):
    - In the <b>`src/config/settings.py`</b> file you need to specify:
        - API key in the <b>`TOKEN`</b> variable:
        ```python
        TOKEN = "HERE YOU CAN PASTE API KEY FOR YOUR BOT"
        ```
        - Full name of your classmates and their tags in the telegram in the dictionary <b>`STUDENTS_DICT`</b>:
        ```python
        STUDENTS_DICT = {
            "k6zma": "Гунин Михаил Александрович",
        }
        ```
        - Full names of all classmates in the list <b>`STUDENTS_LIST`</b>:
        ```python
        STUDENTS_LIST = [
            "Гунин Михаил Александрович",
        ]
        ```
        - List of admins int the list <b>`ADMIN_USERS`</b>:
        ```python
        ADMIN_USERS = ['k6zma', 'maletskayaaa']
        ```
- #### Launching via Docker:
    - To raise a container with a bot you need to write the command:
        ```bash
        docker compose up --build
        ```
- #### Running via Python:
    - First you need to install all the necessary dependencies, to do this you need to write the command:
        ```bash
        pip install -r requirements.txt
        ```
    - Next, to launch the bot, write the command:
        ```bash
        python src/main.py
        ```

I always welcome feedback and suggestions for improving this bot! If you have ideas or find bugs, please create a Pull Request on this repository or contact me directly (tg: @k6zma).