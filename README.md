# dev-settings
Settings for improve dev experience


## VSCode settings
### `settings`
- `User` - Settings that apply globally to any instance of VS Code you open.
- `Workspace` - Settings stored inside your workspace and only apply when the workspace is opened.

> [!WARNING]  
> Workspace settings are specific to a project and override user settings.

```json
    {
        // This configuration add indentation on the explorer view, improving visibility
        "workbench.tree.indent": 30
    }
```
|![alt text](image.png)|
|:--:|
| *Figure 1: With more indentation* |

|![alt text](image-1.png)|
|:--:|
| *Figure 2: Without more indentation* |


### Tree viewing in source control

Click the icon right next to `SOURCE CONTROL`

|![alt text](image-2.png)|
|:--:|
| *Figure 3: Changing the source control viewing by `tree`|