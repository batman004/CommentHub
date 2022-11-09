
```
   ______                                     __  __  __      __
  / ____/___  ____ ___  ____ ___  ___  ____  / /_/ / / /_  __/ /_
 / /   / __ \/ __ `__ \/ __ `__ \/ _ \/ __ \/ __/ /_/ / / / / __ \
/ /___/ /_/ / / / / / / / / / / /  __/ / / / /_/ __  / /_/ / /_/ /
\____/\____/_/ /_/ /_/_/ /_/ /_/\___/_/ /_/\__/_/ /_/\__,_/_.___/


```

# CommentHub CLI

## High Level Workflow of proposed features
![](https://user-images.githubusercontent.com/58564635/199416341-3af9f568-c625-4bbb-ac72-ce9e87bceeb8.png)

**CommentHub** is a `"blazingly" 🔥` fast Command Line Interface to manage commented-out blocks in files and provide version control. built with [Typer](https://typer.tiangolo.com/)

## Installation

To run **CommentHub**, you need to follow the following steps:

1. clone the application's source code to a `CommentHub/` directory
2. Create a Python virtual environment and activate it:

```sh
$ cd CommentHub/
$ python -m venv ./venv
$ source venv/bin/activate
(venv) $
```

3. Install the dependencies:

```sh
(venv) $ python -m pip install -r requirements.txt
```

4. Initialize the application:

run the following script to run database migrations and populate database with required tables
```sh
(venv) $ sh build.sh
```


## Usage

Once you've downloaded the source code and run the installation steps, you can run the following command to access the application's usage description:

```sh
$ python app/main.py --help


 Usage: CommentHub [OPTIONS] COMMAND [ARGS]...

╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --version             -v        Show the application's version and exit.                                                                       │
│ --install-completion            Install completion for the current shell.                                                                      │
│ --show-completion               Show completion for the current shell, to copy it or customize the installation.                               │
│ --help                          Show this message and exit.                                                                                    │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ remove-comments                            Remove commented out code under comment-tag                                                         │
│ retrieve-comments                          Remove commented out code under comment-tag                                                         │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

You can access the help message for specific commands by typing the command and then `--help`. For example, to display the help content for the `add` command, you can run the following:

```sh
$ python app/main.py remove-comments --help

 Usage: CommentHub remove-comments [OPTIONS] FILE_LOCATION

 Remove commented out code under comment-tag

╭─ Arguments ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    file_location      TEXT  [default: None] [required]                                                                                                                        │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

Calling `--help` on each command provides specific and useful information about how to use the command at hand.

## Features

**CommentHub** has the following features:

| Command            | Description                                                  |
| ------------------ | ------------------------------------------------------------
| `retrieve-comments` | Retrieves previous versions of commented out blocks|
| `remove-comments`   | Remove commented out code under comment-tag       |

## Release History

- 0.0.1
  - A work in progress


## Coming up

- [ ] Add persistent database support ⚓
- [ ] Add command to automatically integrate CommentHub with git
- [x] custom comment-tag support 📝





## About the Author

Yuvraj Singh Pathania - [Twitter](https://twitter.com/yuvrajsp01)

Kabir Singh Shekhawat - [Twitter](https://twitter.com/BakedSnek)
