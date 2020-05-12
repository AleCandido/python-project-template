# Python project template

Collect infos & template structure about starting and managing a python project.

## Bootstrapping this template
Instructions to setup step by step a python project starting from this template
(most of the things are already done, but something must be manually customized)

- download/fork this project, and set your remote repo
- *something more still missing*
- go through steps in the next section to properly enable (or disable) all the
    features

### More features

Github pages:
- settings tab: enable deployment from `gh-pages` branch (or your favorite one,
    but remember to fix with the same name the publishing workflow)

Dependencies:
- *package dependencies*: in `setup.py`
- *test dependencies*: in `test_requirements.txt`
- *doc dependencies*: in `doc_requirements.txt`

Docs:
- follow instructions in `docs/bootstrap.md`

Workflows:
- *all the workflows are currently set to run on branch `never` (literally)*
- in order to enable workflows edit their file uncommenting the `on:` section
    and removing the corresponding one pointing to branch `never`

Security (Github):
- *if a private repo*: go to settings and enable read-only privileges for Github
- security tab: enable dependency graph
- security tab: enable dependabot
- customize `SECURITY.md`


## To Do
Something still missing in this project:

- Replace manual bootstrapping
  - add a config file (written in `.yaml`/`.toml`)
  - add a script that makes the bootstrap for you
