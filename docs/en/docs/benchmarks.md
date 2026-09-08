> 🌐 本文档由 [fastapi/fastapi](https://github.com/fastapi/fastapi) 翻译,英文原版见原项目。

# 基准测试 { #benchmarks }

独立的 TechEmpower 基准测试显示,运行在 Uvicorn 之上的 **FastAPI** 应用是[目前最快的 Python 框架之一](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7),仅次于 Starlette 和 Uvicorn 本身(它们是 FastAPI 内部使用的组件)。

不过在查看基准测试和对比数据时,以下几点需要记在心里。

## 基准测试与速度 { #benchmarks-and-speed }

看基准测试时,常见的情况是:把几种不同类型的工具当成等价物来比较。

具体来说,就是把 Uvicorn、Starlette 和 FastAPI 放在一起比(还有其他一大堆工具)。

工具解决的问题越简单,测出来的性能就越好。而且大多数基准测试并不会测试工具提供的附加功能。

层级关系是这样的:

* **Uvicorn**:一个 ASGI 服务器
    * **Starlette**:(使用 Uvicorn)一个 Web 微框架
        * **FastAPI**:(使用 Starlette)一个 API 微框架,为构建 API 提供数据校验等众多附加功能

* **Uvicorn**:
    * 性能最好,因为除了服务器本身,它几乎没有多余的代码。
    * 你不会直接用 Uvicorn 写应用。那意味着你的代码或多或少至少要把 Starlette(或 **FastAPI**)提供的代码全部自己实现一遍。而且如果你真这么干了,最终应用的开销和使用框架、同时精简应用代码和 bug 数量的效果是一样的。
    * 如果要比 Uvicorn,请拿它和 Daphne、Hypercorn、uWSGI 等应用服务器比。
* **Starlette**:
    * 性能仅次于 Uvicorn。实际上,Starlette 就是用 Uvicorn 跑的,所以它之所以"更慢",很可能只是因为要执行更多代码。
    * 但它提供了构建简单 Web 应用的工具,比如基于路径的路由等。
    * 如果要比 Starlette,请拿它和 Sanic、Flask、Django 等 Web 框架(或微框架)比。
* **FastAPI**:
    * 就像 Starlette 用了 Uvicorn 就不可能比它快一样,**FastAPI** 用了 Starlette,也不可能比它快。
    * FastAPI 在 Starlette 之上提供了更多功能,而构建 API 时这些功能几乎总是需要的,比如数据校验和序列化。用了它,你还免费获得自动生成的文档(自动文档甚至不会给运行中的应用增加任何开销,它在启动时就生成好了)。
    * 如果不用 FastAPI 而直接用 Starlette(或 Sanic、Flask、Responder 等其他工具),你就得自己实现全部的数据校验和序列化。所以最终应用的开销其实和使用 FastAPI 构建是一样的。而且在很多情况下,数据校验和序列化恰恰是应用中代码量最大的部分。
    * 因此,使用 FastAPI 能节省开发时间、减少 bug 和代码行数,而性能大概率和不使用它时一样(甚至更好——否则你就得把这些全都写进自己的代码里)。
    * 如果要比 FastAPI,请拿它和提供数据校验、序列化及文档功能的 Web 应用框架(或工具集)比,比如 Flask-apispec、NestJS、Molten 等,也就是内置自动数据校验、序列化和文档功能的框架。
