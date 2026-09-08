> 🌐 本文档由 [fastapi/fastapi](https://github.com/fastapi/fastapi) 翻译,英文原版见原项目。

# FastAPI CLI { #fastapi-cli }

**FastAPI <abbr title="command line interface">CLI</abbr>** 是一个命令行程序,你可以用它来运行 FastAPI 应用、管理 FastAPI 项目,还能做更多事情。

把 FastAPI 加进项目时(例如 `uv add "fastapi[standard]"`),它会附带一个可以在终端里运行的命令行程序。

开发时运行 FastAPI 应用,使用 `fastapi dev` 命令:

<div class="termy">

```console
$ <font color="#4E9A06">fastapi</font> dev

  <span style="background-color:#009485"><font color="#D3D7CF"> FastAPI </font></span>  Starting development server 🚀

             Searching for package file structure from directories with
             <font color="#3465A4">__init__.py</font> files
             Importing from <font color="#75507B">/home/user/code/</font><font color="#AD7FA8">awesomeapp</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> module </font></span>  🐍 main.py

     <span style="background-color:#007166"><font color="#D3D7CF"> code </font></span>  Importing the FastAPI app object from the module with the
             following code:

             <u style="text-decoration-style:solid">from </u><u style="text-decoration-style:solid"><b>main</b></u><u style="text-decoration-style:solid"> import </u><u style="text-decoration-style:solid"><b>app</b></u>

      <span style="background-color:#007166"><font color="#D3D7CF"> app </font></span>  Using import string: <font color="#3465A4">main:app</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Server started at <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000</u></font>
   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Documentation at <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000/docs</u></font>

      <span style="background-color:#007166"><font color="#D3D7CF"> tip </font></span>  Running in development mode, for production use:
             <b>fastapi run</b>

             Logs:

     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Will watch for changes in these directories:
             <b>[</b><font color="#4E9A06">&apos;/home/user/code/awesomeapp&apos;</font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Uvicorn running on <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000</u></font> <b>(</b>Press CTRL+C to
             quit<b>)</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started reloader process <b>[</b><font color="#34E2E2"><b>383138</b></font><b>]</b> using WatchFiles
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started server process <b>[</b><font color="#34E2E2"><b>383153</b></font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Waiting for application startup.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Application startup complete.
```

</div>

/// tip

生产环境请使用 `fastapi run`,而不是 `fastapi dev`。🚀

///

在内部,**FastAPI CLI** 使用的是 [Uvicorn](https://uvicorn.dev),一个高性能、可用于生产环境的 ASGI 服务器。😎

`fastapi` 命令行会尝试自动检测要运行的 FastAPI 应用,默认假设它是 `main.py` 文件(或少数几个其他变体)里一个名为 `app` 的对象。

不过你也可以显式配置要使用的应用。

## 在 `pyproject.toml` 中配置应用 `entrypoint` { #configure-the-app-entrypoint-in-pyproject-toml }

你可以在 `pyproject.toml` 文件中配置应用的位置,比如:

```toml
[tool.fastapi]
entrypoint = "main:app"
```

这个 `entrypoint` 会告诉 `fastapi` 命令按如下方式导入应用:

```python
from main import app
```

如果你的代码结构是这样的:

```
.
├── backend
│   ├── main.py
│   ├── __init__.py
```

那就把 `entrypoint` 设置成:

```toml
[tool.fastapi]
entrypoint = "backend.main:app"
```

这等价于:

```python
from backend.main import app
```

### `fastapi dev` 传路径或使用 `--entrypoint` 命令行选项 { #fastapi-dev-with-path-or-with-entrypoint-cli-option }

你也可以把文件路径直接传给 `fastapi dev` 命令,它会自行猜测要用的 FastAPI 应用对象:

```console
$ uv run fastapi dev main.py
```

或者,给 `fastapi dev` 命令传 `--entrypoint` 选项:

```console
$ uv run fastapi dev --entrypoint main:app
```

但这样一来,每次调用 `fastapi` 命令你都得记得传正确的路径\entrypoint。

另外,其他工具可能找不到它,比如 [VS Code 扩展](editor-support.md)或 [FastAPI Cloud](https://fastapicloud.com),所以推荐使用 `pyproject.toml` 里的 `entrypoint`。

## `fastapi dev` { #fastapi-dev }

运行 `fastapi dev` 会进入开发模式。

默认情况下,**自动重载(auto-reload)**是开启的,你改了代码服务器会自动重载。这比较吃资源,稳定性也不如关闭时。只应在开发时使用。它还监听 IP 地址 `127.0.0.1`,也就是只供本机与自己通信的地址(`localhost`)。

在导入你的应用之前,`fastapi dev` 会把 `FASTAPI_ENV` 环境变量设为 `development`。如果 `FASTAPI_ENV` 已经设置,则保留其现有值。这样应用的启动代码就能选择适合开发的行为,同时你仍然可以提供应用自定义的环境,比如 `staging`。

`FASTAPI_ENV` 的惯用取值是 `development` 和 `production`。`fastapi run` 目前不会改动 `FASTAPI_ENV`,所以如果你的应用需要检测生产模式,请显式设置它。

## `fastapi run` { #fastapi-run }

执行 `fastapi run` 会以生产模式启动 FastAPI。

默认情况下,**自动重载**是关闭的。它监听 IP 地址 `0.0.0.0`,即所有可用的 IP 地址,这样任何能与这台机器通信的人都可以公开访问它。生产环境通常就是这么跑的,比如在容器里。

大多数情况下,你(也应当)会在上层放一个"终结代理(termination proxy)"来处理 HTTPS,具体取决于你的部署方式:服务商可能帮你做了,也可能需要你自己搭建。

/// tip

更多信息见[部署文档](deployment/index.md)。

///
