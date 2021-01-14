# create-go-project

Script to create a simple go project directory structure.

Note that this does NOT follow any standard and is a personal preference. In fact, the generated structure has a `src` directory which is an anti-pattern.

### Usage

1. Copy the script to a suitable location (preferably on PATH).
2. run `python3 create-go-project.py <projectName>`
3. This will create a following heirachy rooted at `<projectName>` in the working directory:

```
projectName
 ┣ config
 ┃ ┗ config.json
 ┣ docs
 ┣ etc
 ┃ ┗ systemd
 ┃ ┃ ┗ system
 ┃ ┃ ┃ ┗ projectName.service
 ┗ src
 ┃ ┗ projectName
 ┃ ┃ ┗ main.go

```
