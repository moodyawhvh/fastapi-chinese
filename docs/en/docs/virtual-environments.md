> 🌐 本文档由 [fastapi/fastapi](https://github.com/fastapi/fastapi) 翻译,英文原版见原项目。

# 虚拟环境 { #virtual-environments }

在做 Python 项目时,你应该使用**虚拟环境**来隔离每个项目各自安装的包。

对于 FastAPI 项目,我推荐使用 [uv](https://docs.astral.sh/uv/) 来管理项目、依赖和虚拟环境。

## 创建项目 { #create-a-project }

按照[官方安装指南](https://docs.astral.sh/uv/getting-started/installation/)安装 `uv`,然后创建一个项目:

<div class="termy">

```console
$ uv init awesome-project --bare
$ cd awesome-project
$ uv add "fastapi[standard]"
```

</div>

`uv` 会自动为项目创建虚拟环境,你不需要自己创建或激活。

使用 `uv run` 在项目环境中运行命令,例如:

<div class="termy">

```console
$ uv run fastapi dev
```

</div>

## 了解更多 { #learn-more }

阅读[虚拟环境指南](https://tiangolo.com/guides/virtual-environments/),了解虚拟环境底层的工作原理,包括激活机制,以及 `python -m venv` 加 `pip` 这套替代方案的工作流程。
