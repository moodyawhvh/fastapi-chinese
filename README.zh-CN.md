<div align="center">

<a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>

# fastapi 中文文档

**FastAPI 框架:高性能、易学、快速编码、生产就绪**

[![原项目](https://img.shields.io/badge/原项目-fastapi--fastapi-blue?style=flat-square&logo=github)](https://github.com/fastapi/fastapi)
[![GitHub Stars](https://img.shields.io/github/stars/fastapi/fastapi?style=flat-square&label=原项目Stars)](https://github.com/fastapi/fastapi/stargazers)
[![PyPI](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)](https://pypi.org/project/fastapi)
[![微信联系](https://img.shields.io/badge/微信-uaycar-brightgreen?style=flat-square&logo=wechat)](#)

</div>

> 本文是 [fastapi/fastapi](https://github.com/fastapi/fastapi) 官方 README 的中文翻译,可能滞后,以原文档为准。

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

- **官方文档**:https://fastapi.tiangolo.com
- **源代码**:https://github.com/fastapi/fastapi

FastAPI 是一个现代、快速(高性能)的 Web 框架,用于基于标准 Python 类型提示构建 API。

## ✨ 核心特性

- **Fast**:性能极高,与 **NodeJS** 和 **Go** 同级(得益于 Starlette 和 Pydantic),是现有最快的 Python 框架之一。
- **Fast to code**:功能开发速度提升约 200% 到 300%。*
- **Fewer bugs**:减少约 40% 的人为(开发者)错误。*
- **Intuitive**:编辑器支持极佳,到处都有自动补全,调试时间更少。
- **Easy**:易于使用和学习,读文档的时间更短。
- **Short**:尽量减少代码重复,每个参数声明带来多项功能。
- **Robust**:直接获得生产就绪的代码,自带自动交互式文档。
- **Standards-based**:基于(并完全兼容)开放 API 标准:[OpenAPI](https://github.com/OAI/OpenAPI-Specification)(前身 Swagger)和 [JSON Schema](https://json-schema.org/)。

<small>* 基于某内部开发团队构建生产应用时的测试估算。</small>

## 💬 用户评价(节选)

- "我计划把 **FastAPI** 用于微软团队的所有 **ML 服务**,部分已集成进 **Windows** 与 **Office** 产品。" —— Kabir Khan,**Microsoft**
- "我们采用 **FastAPI** 构建 REST 服务器,用于查询获取预测结果。" —— Piero Molino 等,**Uber**
- "**Netflix** 很高兴开源基于 **FastAPI** 构建的危机管理编排框架 **Dispatch**!" —— Kevin Glisson 等,**Netflix**
- "要构建生产级 Python API,我强烈推荐 **FastAPI**,设计优雅、易用、可扩展。" —— Deon Pillsbury,**Cisco**

## ⌨️ Typer:命令行界的 FastAPI

如果你要构建的是终端 **CLI** 应用而非 Web API,请看看 [**Typer**](https://typer.tiangolo.com/),它目标是成为 **CLI 界的 FastAPI**。

## 📦 环境要求

- [Starlette](https://starlette.dev/) 负责 Web 部分。
- [Pydantic](https://pydantic.dev/docs/) 负责数据部分。

## 🔧 安装

先[安装 `uv`](https://docs.astral.sh/uv/getting-started/installation/),然后把 FastAPI 添加到项目:

```console
$ uv add "fastapi[standard]"

---> 100%
```

**注意**:`"fastapi[standard]"` 请带引号,保证在所有终端正常工作。若更习惯 `pip`,可在虚拟环境安装 `fastapi[standard]`,替代步骤见[安装指南](tutorial/#install-fastapi)。

## 🚀 示例

### 创建代码

新建 `main.py`:

```Python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

<details>
<summary>或者使用 <code>async def</code>……</summary>

如果你的代码使用 `async` / `await`,请把上述函数改为 `async def` 定义,其余不变。拿不准时查阅文档中 [`async` 与 `await` 的"赶时间?"章节](https://fastapi.tiangolo.com/async/#in-a-hurry)。

</details>

### 运行服务

```console
$ uv run fastapi dev

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
```

命令 `fastapi dev` 会自动读取 `main.py`,检测其中的 FastAPI 应用并用 [Uvicorn](https://uvicorn.dev) 启动服务器;默认开启自动重载,详见 [FastAPI CLI 文档](https://fastapi.tiangolo.com/fastapi-cli/)。

### 验证结果

浏览器访问 [http://127.0.0.1:8000/items/5?q=somequery](http://127.0.0.1:8000/items/5?q=somequery),会看到 JSON 响应:

```JSON
{"item_id": 5, "q": "somequery"}
```

这个 API 在路径 `/` 和 `/items/{item_id}` 上接收 `GET` 请求;`item_id` 是必须为 `int` 的路径参数,`q` 是可选的 `str` 查询参数。

### 交互式 API 文档

访问 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 查看由 [Swagger UI](https://github.com/swagger-api/swagger-ui) 提供的自动交互式文档;访问 [/redoc](http://127.0.0.1:8000/redoc) 查看由 [ReDoc](https://github.com/Redocly/redoc) 提供的另一种自动文档界面。

## 🔄 升级示例

修改 `main.py`,让它接收 `PUT` 请求的请求体,并用标准 Python 类型(Pydantic)声明:

```Python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```

`fastapi dev` 会自动重载,交互式文档同步更新,可在文档页点击 "Try it out" 与 "Execute" 直接调试 API。

### 小结

只需用标准现代 Python 类型**声明一次**参数与请求体的类型,无需学习新语法,即可获得:

- **编辑器支持**:自动补全、类型检查。
- **数据校验**:数据非法时给出清晰错误,支持深层嵌套 JSON。
- **输入转换**:从 JSON、路径/查询参数、Cookie、请求头、表单、文件转为 Python 数据。
- **输出转换**:把 `str`、`int`、`datetime`、`UUID`、数据库模型等转为 JSON 等网络数据。
- **自动交互式文档**:Swagger UI 与 ReDoc,并可基于 OpenAPI 自动生成多语言客户端代码。

教程还包括:请求头/Cookie/表单/文件参数、校验约束、**依赖注入**、**OAuth2 JWT** 认证、深层嵌套 JSON 模型、**GraphQL** 集成,以及 **WebSockets**、极简测试、**CORS** 等。详见[教程 - 用户指南](https://fastapi.tiangolo.com/tutorial/)。

## ☁️ 部署应用(可选)

一条命令即可把应用部署到 [FastAPI Cloud](https://fastapicloud.com)(CLI 会自动检测应用,未登录时打开浏览器完成认证):

```console
$ uv run fastapi deploy
```

FastAPI Cloud 由 FastAPI 原班人马打造,是该项目的主要资金来源;FastAPI 完全开源、基于标准,也可部署到任意云平台。

## ⚡ 性能

TechEmpower 独立基准测试显示,运行在 Uvicorn 下的 **FastAPI** 应用是[现有最快的 Python 框架之一](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7),仅次于其内部依赖的 Starlette 和 Uvicorn。

## 🧩 依赖

`uv add "fastapi[standard]"` 会附带 `standard` 可选依赖组:[`email-validator`](https://github.com/JoshData/python-email-validator)、[`httpx`](https://www.python-httpx.org)、[`jinja2`](https://jinja.palletsprojects.com)、[`python-multipart`](https://github.com/Kludex/python-multipart)、[`uvicorn`](https://uvicorn.dev) 与 `fastapi-cli[standard]`(提供 `fastapi` 命令)。不想要 `standard` 组用 `uv add fastapi`;不要 `fastapi-cloud-cli` 用 `uv add "fastapi[standard-no-fastapi-cloud-cli]"`。其他可选:[`pydantic-settings`](https://pydantic.dev/docs/validation/latest/concepts/pydantic_settings/)、[`orjson`](https://github.com/ijl/orjson)、[`ujson`](https://github.com/ultrajson/ultrajson) 等。

## 📄 许可证

本项目基于 MIT 许可证发布。

---

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

本文档为 [fastapi/fastapi](https://github.com/fastapi/fastapi) 官方 README 的中文翻译,内容版权归原项目作者所有,遵循其原始许可证(MIT)。觉得有用请给原项目点个 Star!⭐
