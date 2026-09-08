> 🌐 本文档由 [fastapi/fastapi](https://github.com/fastapi/fastapi) 翻译,英文原版见原项目。

# 特性 { #features }

## FastAPI 特性 { #fastapi-features }

**FastAPI** 为你提供以下能力:

### 基于开放标准 { #based-on-open-standards }

* 使用 [**OpenAPI**](https://github.com/OAI/OpenAPI-Specification) 创建 API,包括<dfn title="也称为: endpoints, routes">路径</dfn> <dfn title="也称为 HTTP 方法,如 POST、GET、PUT、DELETE">操作</dfn>声明、参数、请求体、安全性等。
* 使用 [**JSON Schema**](https://json-schema.org/) 自动生成数据模型文档(因为 OpenAPI 本身就是基于 JSON Schema 的)。
* 经过细致研究后围绕这些标准而设计,而不是事后在上面加的一层补丁。
* 这也使得在多种语言中自动进行**客户端代码生成**成为可能。

### 自动生成文档 { #automatic-docs }

交互式 API 文档与探索式 Web 用户界面。框架基于 OpenAPI,可选方案有很多,默认内置两种。

* [**Swagger UI**](https://github.com/swagger-api/swagger-ui):交互式探索,直接在浏览器里调用和测试你的 API。

![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

* 备选的 API 文档方案 [**ReDoc**](https://github.com/Redocly/redoc)。

![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### 纯正的现代 Python { #just-modern-python }

一切都基于标准的 **Python 类型**声明(多亏了 Pydantic)。没有需要学习的新语法,就是标准的现代 Python。

如果你需要用 2 分钟复习一下 Python 类型的用法(即使你不用 FastAPI),看看这个简短教程:[Python 类型](python-types.md)。

你只需书写带类型的标准 Python:

```Python
from datetime import date

from pydantic import BaseModel

# Declare a variable as a str
# and get editor support inside the function
def main(user_id: str):
    return user_id


# A Pydantic model
class User(BaseModel):
    id: int
    name: str
    joined: date
```

随后可以这样使用:

```Python
my_user: User = User(id=3, name="John Doe", joined="2018-07-19")

second_user_data = {
    "id": 4,
    "name": "Mary",
    "joined": "2018-11-30",
}

my_second_user: User = User(**second_user_data)
```

/// note

`**second_user_data` 的意思是:

把 `second_user_data` 字典的键和值直接作为关键字参数传入,等价于:`User(id=4, name="Mary", joined="2018-11-30")`

///

### 编辑器支持 { #editor-support }

整个框架的设计目标就是易用、直观,所有设计决策甚至在开发开始之前就已在多个编辑器中测试过,以确保最佳开发体验。

在 Python 开发者调查中,[使用最多的功能之一显然是"自动补全"](https://www.jetbrains.com/research/python-developers-survey-2017/#tools-and-features)。

整个 **FastAPI** 框架就是为满足这一点而设计的。自动补全无处不在。

你几乎不需要再回头翻文档。

编辑器可以这样帮你:

* 在 [Visual Studio Code](https://code.visualstudio.com/) 中:

![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)

* 在 [PyCharm](https://www.jetbrains.com/pycharm/) 中:

![editor support](https://fastapi.tiangolo.com/img/pycharm-completion.png)

你甚至能在以前觉得不可能的地方获得补全。比如,来自请求的 JSON 体内(可能是深层嵌套的)`price` 键。

再也不用敲错键名、来回翻文档,或者上下滚动确认自己到底用的是 `username` 还是 `user_name` 了。

### 简短 { #short }

每一处都有合理的**默认值**,同时又处处提供可选配置。所有参数都可以细调,按你的需求定制 API。

但默认情况下,一切**"开箱即用"**。

### 数据校验 { #validation }

* 对大多数(或者说全部?)Python **数据类型**进行校验,包括:
    * JSON 对象(`dict`)。
    * 定义了元素类型的 JSON 数组(`list`)。
    * 定义了最小/最大长度的字符串(`str`)字段。
    * 带最小值/最大值等的数字(`int`、`float`)。

* 对更特殊的类型进行校验,比如:
    * URL。
    * Email。
    * UUID。
    * ……以及其他。

所有校验都由久经考验、健壮可靠的 **Pydantic** 处理。

### 安全性与认证 { #security-and-authentication }

安全与认证开箱集成,不与任何数据库或数据模型绑定。

支持 OpenAPI 中定义的所有安全方案,包括:

* HTTP Basic。
* **OAuth2**(也支持 **JWT token**)。参见教程 [OAuth2 with JWT](tutorial/security/oauth2-jwt.md)。
* API 密钥,可位于:
    * 请求头(Headers)。
    * 查询参数(Query parameters)。
    * Cookie 等等。

外加 Starlette 的全部安全特性(包括 **session cookie**)。

所有这些都构建为可复用的工具和组件,易于与你的系统、数据存储、关系型和 NoSQL 数据库等集成。

### 依赖注入 { #dependency-injection }

FastAPI 内置一套极其易用却又极其强大的 <dfn title='也称为 "components"、"resources"、"services"、"providers"'><strong>依赖注入</strong></dfn>系统。

* 依赖自身还可以再依赖其他依赖,形成层级或**依赖"图"**。
* 一切由框架**自动处理**。
* 所有依赖都可以从请求中获取数据,并**增强路径操作**的约束和自动文档。
* 连依赖中定义的*路径操作*参数都支持**自动校验**。
* 支持复杂的用户认证系统、**数据库连接**等。
* 对数据库、前端等**不作任何强制绑定**,但又能与它们轻松集成。

### 无限量"插件" { #unlimited-plug-ins }

或者换句话说:根本不需要插件,直接导入并使用你需要的代码即可。

任何集成的设计都简单到(借助依赖系统)你只需用和*路径操作*相同的结构与语法,写 2 行代码就能为应用造出一个"插件"。

### 经过充分测试 { #tested }

* 100% 的<dfn title="被自动测试覆盖的代码量">测试覆盖率</dfn>。
* 100% <dfn title="Python 类型注解,有了它你的编辑器和外部工具才能给你更好的支持">类型注解化</dfn>的代码库。
* 已在生产应用中使用。

## Starlette 特性 { #starlette-features }

**FastAPI** 与 [**Starlette**](https://starlette.dev/) 完全兼容(并且基于它)。所以你已有的任何 Starlette 代码同样可用。

`FastAPI` 实际上是 `Starlette` 的子类。所以如果你已经了解或正在使用 Starlette,大部分功能的表现方式都一样。

使用 **FastAPI**,你能获得 **Starlette** 的全部特性(FastAPI 就是打了鸡血的 Starlette):

* 真正惊艳的性能。它是[最快的 Python 框架之一,与 **NodeJS** 和 **Go** 相当](https://github.com/encode/starlette#performance)。
* **WebSocket** 支持。
* 进程内后台任务。
* 启动与关闭事件。
* 基于 HTTPX 的测试客户端。
* **CORS**、GZip、静态文件、流式响应。
* **Session 与 Cookie** 支持。
* 100% 测试覆盖率。
* 100% 类型注解化代码库。

## Pydantic 特性 { #pydantic-features }

**FastAPI** 与 [**Pydantic**](https://pydantic.dev/docs/) 完全兼容(并且基于它)。所以你已有的任何 Pydantic 代码同样可用。

包括同样基于 Pydantic 的外部库,比如数据库的 <abbr title="Object-Relational Mapper">ORM</abbr> 和 <abbr title="Object-Document Mapper">ODM</abbr>。

这也意味着,很多情况下你可以把从请求中获得的对象**直接传给数据库**,因为一切都已自动校验过。

反过来同理,很多情况下你可以把从数据库取出的对象**直接返回给客户端**。

使用 **FastAPI**,你能获得 **Pydantic** 的全部特性(FastAPI 所有数据处理都基于 Pydantic):

* **无需折磨自己**:
    * 不需要学新的模式定义微语言。
    * 懂 Python 类型,就懂怎么用 Pydantic。
* 与你的 **<abbr title="Integrated Development Environment: similar to a code editor">IDE</abbr>/<dfn title="A program that checks for code errors">linter</dfn>/大脑**配合顺畅:
    * Pydantic 的数据结构就是你定义的类的实例;自动补全、lint、mypy 和你的直觉都能正常作用于校验后的数据。
* 校验**复杂结构**:
    * 使用层级化的 Pydantic 模型、Python `typing` 的 `List`、`Dict` 等。
    * validator(校验器)让复杂的数据模式能被清晰、轻松地定义、检查,并输出为 JSON Schema 文档。
    * 深层**嵌套的 JSON** 对象也能全部校验并标注。
* **可扩展**:
    * Pydantic 允许自定义数据类型,也可以用 validator 装饰器装饰模型方法来扩展校验。
* 100% 测试覆盖率。
