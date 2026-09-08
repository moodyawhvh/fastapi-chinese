"""FastAPI framework, high performance, easy to learn, fast to code, ready for production"""

__version__ = "0.141.1"

# 状态码常量:直接复用 Starlette 的 status 模块(如 status.HTTP_200_OK)
from starlette import status as status

# ============ 核心应用与路由 ============
# FastAPI 应用主类(继承自 Starlette),项目的总入口
from .applications import FastAPI as FastAPI
# APIRouter:路由分组器,用于模块化组织路径操作
from .routing import APIRouter as APIRouter

# ============ 请求 / 响应与后台任务 ============
# 请求对象与响应对象:路径操作函数中直接访问请求细节或自定义响应
from .requests import Request as Request
from .responses import Response as Response
# 后台任务:响应返回后在后台继续执行的任务集合
from .background import BackgroundTasks as BackgroundTasks
# 上传文件的数据结构封装
from .datastructures import UploadFile as UploadFile

# ============ 异常 ============
# HTTPException:带状态码与详细信息的 HTTP 异常
from .exceptions import HTTPException as HTTPException
# WebSocketException:WebSocket 场景的异常(如关闭连接时附带状态码)
from .exceptions import WebSocketException as WebSocketException

# ============ 参数声明函数 ============
# 这些函数用于路径操作函数的参数上,声明参数来源与校验规则:
# Body/ Form/ File:请求体、表单、文件
# Query/ Path/ Header/ Cookie:查询参数、路径参数、请求头、Cookie
# Depends:声明依赖项;Security:带安全方案的依赖项
from .param_functions import Body as Body
from .param_functions import Cookie as Cookie
from .param_functions import Depends as Depends
from .param_functions import File as File
from .param_functions import Form as Form
from .param_functions import Header as Header
from .param_functions import Path as Path
from .param_functions import Query as Query
from .param_functions import Security as Security

# ============ WebSocket ============
# WebSocket 会话对象,以及连接断开时抛出的异常
from .websockets import WebSocket as WebSocket
from .websockets import WebSocketDisconnect as WebSocketDisconnect
