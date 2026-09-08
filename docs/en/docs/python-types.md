> 🌐 本文档由 [fastapi/fastapi](https://github.com/fastapi/fastapi) 翻译,英文原版见原项目。
>
> ⚠️ 说明:本文档篇幅较长(超过 10000 字符),按汉化预算仅翻译核心章节;其余细节请参阅英文原版。

# Python 类型入门 { #python-types-intro }

Python 支持可选的"类型提示"(也叫"类型注解")。

这些**"类型提示"**或注解是一种特殊语法,用来声明变量的<dfn title="例如: str, int, float, bool">类型</dfn>。

为变量声明类型后,编辑器和工具就能给你更好的支持。

这只是一份关于 Python 类型提示的**快速教程 / 复习**,只覆盖配合 **FastAPI** 使用所需的最少知识……实际上真的很少。

**FastAPI** 完全建立在这些类型提示之上,它们带来了大量优势。

但即使你从不使用 **FastAPI**,学一点类型提示也会让你受益。

/// note

如果你是 Python 专家,已经完全掌握类型提示,可以直接跳到下一章。

///

## 动机 { #motivation }

从一个简单的例子开始:

{* ../../docs_src/python_types/tutorial001_py310.py *}

运行这个程序会输出:

```
John Doe
```

这个函数做了以下事情:

* 接收 `first_name` 和 `last_name`。
* 用 `title()` 把两者首字母转为大写。
* <dfn title="Puts them together, as one. With the contents of one after the other.">拼接</dfn>两个字符串,中间用空格分隔。

{* ../../docs_src/python_types/tutorial001_py310.py hl[2] *}

### 修改它 { #edit-it }

程序很简单。但想象一下你正在从头写它。

写到一半定义函数,参数准备好了……

接着要调用"那个把首字母转大写的方法"。

是 `upper`?`uppercase`?`first_uppercase`?还是 `capitalize`?

这时你请出程序员的老朋友:编辑器自动补全。

输入函数第一个参数 `first_name`,敲一个点(`.`),再按 `Ctrl+Space` 触发补全。

遗憾的是,你什么都得不到:

<img src="/img/python-types/image01.png">

### 加上类型 { #add-types }

只改一行。把函数参数从:

```Python
    first_name, last_name
```

改成:

```Python
    first_name: str, last_name: str
```

就这样。这些就是"类型提示":

{* ../../docs_src/python_types/tutorial002_py310.py hl[1] *}

注意,这和声明默认值不一样:

```Python
    first_name="john", last_name="doe"
```

这是两回事。我们用的是冒号(`:`),不是等号(`=`)。

加上类型提示通常不会改变程序的行为。

但现在再想象你在写那个函数,这次带着类型提示。同样位置按 `Ctrl+Space`,你会看到:

<img src="/img/python-types/image02.png">

于是可以滚动浏览候选,直到找到那个"眼熟"的:

<img src="/img/python-types/image03.png">

## 更多的动机 { #more-motivation }

看这个已经带了类型提示的函数:

{* ../../docs_src/python_types/tutorial003_py310.py hl[1] *}

因为编辑器知道变量的类型,你不仅获得补全,还获得错误检查:

<img src="/img/python-types/image04.png">

现在你知道必须修复它,用 `str(age)` 把 `age` 转成字符串:

{* ../../docs_src/python_types/tutorial004_py310.py hl[2] *}

## 声明类型 { #declaring-types }

你已经看到了声明类型提示的主要位置:函数参数。

这也是在 **FastAPI** 中使用它们的主要位置。

### 简单类型 { #simple-types }

你可以声明所有标准 Python 类型,不只是 `str`。例如:

* `int`
* `float`
* `bool`
* `bytes`

{* ../../docs_src/python_types/tutorial005_py310.py hl[1] *}

### `typing` 模块 { #typing-module }

某些场景下,你可能需要从标准库 `typing` 模块导入一些东西。比如想声明"任意类型"时,可以使用 `typing` 的 `Any`:

```python
from typing import Any


def some_function(data: Any):
    print(data)
```

### 泛型类型 { #generic-types }

有些类型可以在方括号里接收"类型参数"来定义其内部类型,例如"字符串列表"声明为 `list[str]`。

这种能接收类型参数的类型叫**泛型类型(Generic types)**或**泛型(Generics)**。

以下内置类型都可以当泛型用(方括号里放类型):

* `list`
* `tuple`
* `set`
* `dict`

#### List { #list }

例如定义一个变量为 `str` 组成的 `list`。用同样的冒号(`:`)语法声明变量,类型写 `list`,因为 list 是包含内部类型的类型,所以把内部类型放进方括号:

{* ../../docs_src/python_types/tutorial006_py310.py hl[1] *}

/// note

方括号里的那些内部类型叫"类型参数"。

本例中,`str` 是传给 `list` 的类型参数。

///

这意味着:"变量 `items` 是一个 `list`,列表中的每一项都是 `str`"。

这样一来,即使在遍历列表元素时,编辑器也能提供支持:

<img src="/img/python-types/image05.png">

没有类型注解,这几乎不可能做到。

注意变量 `item` 是列表 `items` 中的一个元素,编辑器仍然知道它是 `str`,并据此提供支持。

#### Tuple 和 Set { #tuple-and-set }

声明 `tuple` 和 `set` 也是同样的做法:

{* ../../docs_src/python_types/tutorial007_py310.py hl[1] *}

这表示:

* 变量 `items_t` 是一个有 3 个元素的 `tuple`:一个 `int`、另一个 `int`、一个 `str`。
* 变量 `items_s` 是一个 `set`,其每个元素都是 `bytes` 类型。

#### Dict { #dict }

定义 `dict` 时传入 2 个类型参数,用逗号分隔。第一个对应 `dict` 的键,第二个对应 `dict` 的值:

{* ../../docs_src/python_types/tutorial008_py310.py hl[1] *}

这表示:

* 变量 `prices` 是一个 `dict`:
    * 键的类型是 `str`(比如每种商品的名字)。
    * 值的类型是 `float`(比如每种商品的价格)。

#### Union { #union }

你可以声明一个变量可以是**几种类型**之一,比如 `int` 或 `str`。

用<dfn title='also called "bitwise or operator", but that meaning is not relevant here'>竖线(`|`)</dfn>分隔两个类型即可。

这叫"联合(union)",因为变量可以取这两组类型并集中的任何值。

```Python hl_lines="1"
{!> ../../docs_src/python_types/tutorial008b_py310.py!}
```

也就是说 `item` 可以是 `int` 也可以是 `str`。

#### 可能为 `None` { #possibly-none }

你还可以声明一个值可以是某个类型(比如 `str`),但也可以是 `None`。

//// tab | Python 3.10+

```Python hl_lines="1"
{!> ../../docs_src/python_types/tutorial009_py310.py!}
```

////

用 `str | None` 而不是只写 `str`,编辑器就能帮你发现这类错误:你默认值永远是 `str`,而它实际上还可能是 `None`。

### 类作为类型 { #classes-as-types }

你也可以把一个类声明为变量的类型。

假设有一个 `Person` 类,带有名字:

{* ../../docs_src/python_types/tutorial010_py310.py hl[1:3] *}

然后声明一个 `Person` 类型的变量:

{* ../../docs_src/python_types/tutorial010_py310.py hl[6] *}

再次地,所有编辑器支持都到位了:

<img src="/img/python-types/image06.png">

注意,这表示"`one_person` 是 `Person` 类的一个**实例**",而不是"`one_person` 是名为 `Person` 的**类**"。

## Pydantic 模型 { #pydantic-models }

[Pydantic](https://pydantic.dev/docs/) 是一个执行数据校验的 Python 库。

你把数据的"形状"声明为带属性的类,每个属性都有类型。

然后用一些值创建该类的实例,它会校验这些值、将其转换为合适的类型(如需要),并返回一个携带全部数据的对象。

对这个结果对象,你能享受全部编辑器支持。

一个来自 Pydantic 官方文档的例子:

{* ../../docs_src/python_types/tutorial011_py310.py *}

/// note

想了解更多,请查阅 [Pydantic 文档](https://pydantic.dev/docs/)。

///

**FastAPI** 完全基于 Pydantic。

你会在[教程 - 用户指南](tutorial/index.md)里看到更多实际用法。

## 带元数据注解的类型提示 { #type-hints-with-metadata-annotations }

Python 还支持用 `Annotated` 在类型提示中附加**额外的<dfn title="Data about the data, in this case, information about the type, e.g. a description.">元数据</dfn>**。

从 `typing` 导入 `Annotated`:

{* ../../docs_src/python_types/tutorial013_py310.py hl[1,4] *}

Python 本身对 `Annotated` 不会做任何事。对编辑器和其他工具而言,类型依然是 `str`。

但你可以利用 `Annotated` 里的这个空间,向 **FastAPI** 提供关于应用行为的额外元数据。

关键是记住:**传给 `Annotated` 的第一个*类型参数***才是**实际类型**,其余的只是给其他工具用的元数据。

现在你只需知道 `Annotated` 存在,而且它是标准 Python。😎

之后你会看到它有多**强大**。

/// tip

它是**标准 Python**,意味着你在编辑器里、在分析和重构代码的工具中,仍然能获得**最好的开发体验**。✨

你的代码也能与众多其他 Python 工具和库高度兼容。🚀

///

## **FastAPI** 中的类型提示 { #type-hints-in-fastapi }

**FastAPI** 利用这些类型提示完成很多事情。

用 **FastAPI** 声明带类型提示的参数,你能得到:

* **编辑器支持**。
* **类型检查**。

……而 **FastAPI** 用同样的声明来:

* **定义要求**:来自请求的路径参数、查询参数、请求头、请求体、依赖等。
* **转换数据**:把请求数据转换成所需的类型。
* **校验数据**:来自每个请求的数据:
    * 数据无效时自动生成**错误信息**返回给客户端。
* 使用 OpenAPI **生成文档**:
    * 随后被自动交互式文档界面使用。

这些听起来可能很抽象。别担心,你会在[教程 - 用户指南](tutorial/index.md)里看到它们全部落地。

重点是:只使用标准 Python 类型、只写在一个地方(不用添加更多类、装饰器等),**FastAPI** 就会替你完成大量工作。

/// note

如果你已经读完整个教程、回来想深入了解类型,[`mypy` 的"速查表"](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)是不错的资源。

///
