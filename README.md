# dev-settings

Sometimes we just leave out configurations that certainly could improve our `Dev Experience`, like some easy configurations on `VSCode` itself. This repository aims to share some settings and tools that I myself think are extremely helpful.

## Using `Makefile`

`Makefile` is useful for automating tasks, like creating a python environment

## VSCode settings

### `settings.json`
- `User` - Settings that apply globally to any instance of VS Code you open.
- `Workspace` - Settings stored inside your workspace and only apply when the workspace is opened.

Look at the `.vscode/settings.json` for the configurations

> [!WARNING]
> Workspace settings are specific to a project and override user settings.

|![alt text](./_statics/images/with-ident.png)|
|:--:|
| *Figure 1: With more indentation* |

|![alt text](./_statics/images/without-ident.png)|
|:--:|
| *Figure 2: Default value* |


### Tree viewing in source control

Click the icon right next to `SOURCE CONTROL`

|![alt text](./_statics/images/tree-view-source-control.png)|
|:--:|
| *Figure 3: Changing the source control viewing by `tree`*|

## VSCode extensions

Below are a list of extremely useful extensions:
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) (will install `Pylance` and `Python Debugger`, which also have some settings)
- [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
- [Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
- [Code Spell checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) (available in others languages as well)
- [Github Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
- [Git graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
- [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)


## Miscellaneous

- Use `alt + ←,→` to move between words
- Use `ctrl + D` to select the next occurrence of the selected word
- Use `ctrl + shift + L` to select all occurrences of the selected word
- Use the `Column selection mode` for selecting multiple lines at once
