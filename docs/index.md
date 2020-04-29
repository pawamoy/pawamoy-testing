# Pawamoy Testing
![ci](https://github.com/pawamoy/pawamoy-testing/workflows/ci/badge.svg)
[![documentation](https://img.shields.io/readthedocs/pawamoy-testing.svg?style=flat)](https://pawamoy-testing.readthedocs.io/en/latest/index.html)
[![pypi version](https://img.shields.io/pypi/v/pawamoy-testing.svg)](https://pypi.org/project/pawamoy-testing/)

Testing this great template

## Requirements
Pawamoy Testing requires Python 3.6 or above.

<details>
<summary>To install Python 3.6, I recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.</summary>

```bash
# install pyenv
git clone https://github.com/pyenv/pyenv ~/.pyenv

# setup pyenv (you should also put these three lines in .bashrc or similar)
export PATH="${HOME}/.pyenv/bin:${PATH}"
export PYENV_ROOT="${HOME}/.pyenv"
eval "$(pyenv init -)"

# install Python 3.6
pyenv install 3.6.8

# make it available globally
pyenv global system 3.6.8
```
</details>

## Installation
With `pip`:
```bash
python3.6 -m pip install pawamoy-testing
```

With [`pipx`](https://github.com/pipx-project/pipx):
```bash
python3.6 -m pip install --user pipx

pipx install --python python3.6 pawamoy-testing
```
