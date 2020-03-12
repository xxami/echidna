## echidna.py
quick reference for python gaijins setting up a discord.py bot using tools that make sense in 2020

## step 0 - install python 3
python 2 is over, let's make sure we're running with python 3 (https://www.python.org/downloads/)

```sh
$ python --version
> Python 3.7.4
```

## step 1 - the package manager
discord.py is not included as part of pythons standard library, so we could use a package manager
to pull it in - can always source it manually, but it's generally easier to let a tool do it.
i'll use the flavour of the month: poetry - install here: https://python-poetry.org/docs/

```sh
$ poetry --version
> Poetry version 1.0.5
```

## step 2 - create a new project
make it simple, using poetry:

```sh
$ poetry new echidnabot
$ cd echidnabot
```

poetry will kindly generate a project file and basic project structure - part of that
is installing pytest for us - a module we can use to unit test our projects. let's try it out

```sh
$ poetry install
$ poetry run pytest tests
```

great, we've got tests that can refer to our project and pass! we don't yet have a
functional application, so let's change that:

```sh
$ cd echidnabot
$ echo "def init(): print('nyaa~ world')" >> main.py
$ cat main.py
$ cd ..
```

we can add an entry point to help us run our code in `pyproject.toml`:

```
[tool.poetry.scripts]
start = "echidnabot.main:init"
```

and run simply by: `$ poetry run start`

## step 3 - write the bot of your dreams!

musn't forget the part where we add discord.py to the project:

```sh
$ poetry add discord.py
```

see /echidnabot/ for full example code!