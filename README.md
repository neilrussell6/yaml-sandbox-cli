yaml-sandbox-cli
===

> This is sandbox for messing around with YAML

setup
---

### Virtual env

setup a virtual environment:
```bash
sudo apt-get install -y python3-venv
python3 -m venv venv
source venv/bin/activate
```

optional: add an alias to ``.bash_aliases``
```bash
alias activate="source venv/bin/activate/"
```

### Usage

```bash
yaml-sandbox-cli parse --file data/aliases.yml
yaml-sandbox-cli parse --file data/merging.yml
yaml-sandbox-cli parse --file data/test1.yml
yaml-sandbox-cli parse --file data/env-vars.yml
```

testing
---

Run all tests like this:
```bash
make test
 ```
