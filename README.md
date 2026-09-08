<div align="center">

# fastapi 中文翻译版

**[中文版] fastapi — 高性能、易学、快速编码、生产就绪的 Python Web API 框架**

[![原项目](https://img.shields.io/badge/原项目-fastapi--fastapi-blue?style=flat-square&logo=github)](https://github.com/fastapi/fastapi)
[![中文文档](https://img.shields.io/badge/中文文档-README.zh--CN.md-orange?style=flat-square)](README.zh-CN.md)
[![GitHub Stars](https://img.shields.io/github/stars/fastapi/fastapi?style=flat-square&label=原项目Stars)](https://github.com/fastapi/fastapi/stargazers)
[![微信联系](https://img.shields.io/badge/微信-uaycar-brightgreen?style=flat-square&logo=wechat)](#)

</div>

---

> 这是 [fastapi/fastapi](https://github.com/fastapi/fastapi) 的中文翻译版本。
> 完整源代码请访问原项目:https://github.com/fastapi/fastapi

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

---

## 📖 项目简介

FastAPI 是一个现代、快速(高性能)的 Python Web 框架,用于构建 API,基于标准 Python 类型提示。它底层依托 Starlette 处理 Web 部分、Pydantic 处理数据部分,性能可与 NodeJS 和 Go 比肩。你只需声明一次参数类型,就能自动获得数据校验、序列化转换和交互式 API 文档,开发体验和 生产效率都非常出色。

## ✨ 主要特性

- **极致性能**:与 NodeJS、Go 同级的高性能,是现有最快的 Python 框架之一(得益于 Starlette 和 Pydantic)。
- **开发提速**:编码速度提升约 200%~300%,功能落地更快。
- **更少 Bug**:减少约 40% 的人为(开发者)错误。
- **智能提示**:编辑器支持极佳,到处都有自动补全,调试时间大幅减少。
- **简单易学**:设计上追求易用易学,读文档的时间更短。
- **代码精简**:最大限度减少代码重复,每个参数声明带来多项功能,Bug 更少。
- **生产就绪**:直接获得可用于生产的代码,自带自动交互式文档。
- **基于标准**:完全兼容开放 API 标准 OpenAPI(前身为 Swagger)与 JSON Schema。

## 📁 文件说明

| 文件 | 说明 |
|:-----|:-----|
| README.md | 本文件(中文简介) |
| README.zh-CN.md | 详细中文文档(完整汉化) |

## 🚀 快速开始

1. 先安装 [uv](https://docs.astral.sh/uv/getting-started/installation/),然后把 FastAPI 加入你的项目:

```console
$ uv add "fastapi[standard]"
```

2. 创建 `main.py`:

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

3. 启动开发服务器:

```console
$ uv run fastapi dev
```

4. 打开浏览器访问 http://127.0.0.1:8000/items/5?q=somequery ,即可看到 JSON 响应:

```JSON
{"item_id": 5, "q": "somequery"}
```

5. 访问 http://127.0.0.1:8000/docs 查看自动生成的交互式 API 文档(Swagger UI),访问 /redoc 可查看 ReDoc 版本。

6. 一条命令即可部署到 [FastAPI Cloud](https://fastapicloud.com)(可选):

```console
$ uv run fastapi deploy
```

完整源代码与最新版本请访问原项目:https://github.com/fastapi/fastapi

## 📞 联系方式

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

---

本项目为 [fastapi/fastapi](https://github.com/fastapi/fastapi) 的中文翻译版本,所有代码版权归原项目作者所有,遵循其原始许可证(MIT)。

**如果觉得有用,请给原项目点个 Star!** ⭐
