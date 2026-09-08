> 🌐 本文档由 [fastapi/fastapi](https://github.com/fastapi/fastapi) 翻译,英文原版见原项目。

# 编辑器支持 { #editor-support }

官方的 [FastAPI 扩展](https://marketplace.visualstudio.com/items?itemName=FastAPILabs.fastapi-vscode)为你的 FastAPI 开发工作流增色不少:*路径操作*的发现与导航、FastAPI Cloud 部署,以及实时日志流。

关于该扩展的更多细节,请参阅 [GitHub 仓库](https://github.com/fastapi/fastapi-vscode)上的 README。

## 安装与设置 { #setup-and-installation }

**FastAPI 扩展**同时支持 [VS Code](https://code.visualstudio.com/) 和 [Cursor](https://www.cursor.com/)。可以在各编辑器的扩展面板中直接安装:搜索 "FastAPI",选择 **FastAPI Labs** 发布的那个扩展即可。该扩展也能在浏览器版编辑器中使用,比如 [vscode.dev](https://vscode.dev) 和 [github.dev](https://github.dev)。

### 应用发现 { #application-discovery }

默认情况下,扩展会自动扫描工作区中实例化了 `FastAPI()` 的文件来发现 FastAPI 应用。如果自动检测不适应你的项目结构,你可以在 `pyproject.toml` 中通过 `[tool.fastapi]` 指定入口,或者用 `fastapi.entryPoint` 这个 VS Code 设置以模块记法指定(例如 `myapp.main:app`)。

## 功能 { #features }

- **路径操作浏览器(Path Operation Explorer)** - 侧边栏树形视图,展示应用中所有<dfn title="routes, endpoints">*路径操作*</dfn>。点击即可跳转到任意路由或 router 的定义。
- **路由搜索** - 按路径、方法或名称搜索,快捷键 <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>E</kbd>(macOS 上是 <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>E</kbd>)。
- **CodeLens 导航** - 测试客户端调用(例如 `client.get('/items')`)上方会出现可点击链接,直接跳转到对应的*路径操作*,方便在测试与实现之间快速切换。
- **部署到 FastAPI Cloud** - 一键把应用部署到 [FastAPI Cloud](https://fastapicloud.com/)。
- **应用日志流** - 实时流式查看部署在 FastAPI Cloud 上的应用日志,支持级别过滤和文本搜索。

如果你想熟悉一下这个扩展的功能,可以打开命令面板(<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>,macOS 上是 <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>),选择 "Welcome: Open walkthrough...",然后选中 "Get started with FastAPI" 演练教程。
