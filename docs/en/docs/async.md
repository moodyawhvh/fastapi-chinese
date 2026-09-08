> 🌐 本文档由 [fastapi/fastapi](https://github.com/fastapi/fastapi) 翻译,英文原版见原项目。
>
> ⚠️ 说明:本文档篇幅较长(超过 10000 字符),按汉化预算翻译核心章节,文末"Very Technical Details"一节仅作摘译,完整细节请参阅英文原版。

# 并发与 async / await { #concurrency-and-async-await }

关于*路径操作函数*的 `async def` 语法的细节,以及异步代码、并发与并行的一些背景知识。

## 赶时间? { #in-a-hurry }

<abbr title="too long; didn't read"><strong>TL;DR:</strong></abbr>

如果你使用的第三方库要求你用 `await` 调用它,比如:

```Python
results = await some_library()
```

那么请用 `async def` 声明你的*路径操作函数*:

```Python hl_lines="2"
@app.get('/')
async def read_results():
    results = await some_library()
    return results
```

/// note

`await` 只能在用 `async def` 创建的函数内部使用。

///

---

如果你使用的第三方库要与其他东西通信(数据库、API、文件系统等),但不支持 `await`(目前大多数数据库库都是如此),那么请像平常一样用普通的 `def` 声明*路径操作函数*:

```Python hl_lines="2"
@app.get('/')
def results():
    results = some_library()
    return results
```

---

如果你的应用(不知怎的)不需要和任何外部东西通信并等待响应,那就用 `async def`,即使函数内部并不需要 `await`。

---

如果你就是拿不准,就用普通的 `def`。

---

**注意**:*路径操作函数*里 `def` 和 `async def` 可以随意混搭,每个函数都选对你来说最合适的方式。FastAPI 会正确处理它们。

无论如何,在上面任何一种情况下,FastAPI 仍然会异步工作,并且速度飞快。

但遵循上述步骤,它还能做一些性能优化。

## 技术细节 { #technical-details }

现代 Python 支持**"异步代码"**,靠的是一种叫**"协程(coroutine)"**的机制,以及 **`async` 和 `await`** 语法。

我们把这句话拆开,在下面几节里逐个看:

* **异步代码(Asynchronous Code)**
* **`async` 和 `await`**
* **协程(Coroutines)**

## 异步代码 { #asynchronous-code }

异步代码的意思是:语言 💬 有一种方式告诉计算机 / 程序 🤖,在代码的某个位置,它 🤖 需要等待*别处的某个东西*完成。姑且把那个*别的东西*叫"慢文件" 📝。

在这段等待时间里,计算机可以去干别的活,同时让"慢文件" 📝 慢慢完成。

然后,计算机 / 程序 🤖 每逢有机会(比如又在等什么了,或者把手头的活干完了)就会回来看看它 🤖 等待的任务有没有完成,并做好善后。

接着,它 🤖 拿起第一个完成的任务(比如我们的"慢文件" 📝),继续处理它该做的事。

这种"等待别的东西"通常指的是相对"慢"的<abbr title="Input and Output">I/O</abbr> 操作(与处理器和内存的速度相比),比如等待:

* 客户端的数据通过网络传过来
* 你的程序发出的数据通过网络被客户端接收
* 磁盘上文件的内容被系统读取并交给你的程序
* 你的程序交给系统的内容被写入磁盘
* 一个远程 API 操作
* 一个数据库操作完成
* 一个数据库查询返回结果
* 等等

由于执行时间主要消耗在等待 <abbr title="Input and Output">I/O</abbr> 操作上,这类操作被称为"I/O 密集型(I/O bound)"操作。

之所以叫"异步(asynchronous)",是因为计算机 / 程序不必和慢任务"同步",不必傻等着、什么也不做,非要在任务完成的那一刻才能拿结果继续干活。

作为一个"异步"系统,任务完成后只需稍作排队(几微秒),等计算机 / 程序把手头的事做完,就会回来取走结果并继续处理。

与"异步"相对的"同步(synchronous)",常被称为"顺序(sequential)",因为计算机 / 程序按顺序执行所有步骤后才切换到别的任务,哪怕这些步骤包含等待。

### 并发与汉堡 { #concurrency-and-burgers }

上面描述的**异步**代码,有时也被称为**"并发(concurrency)"**。它不同于**"并行(parallelism)"**。

**并发**和**并行**都与"多件事或多或少同时发生"有关。

但*并发*和*并行*的细节相当不同。

要看清差异,想象下面这个关于汉堡的故事:

### 并发汉堡 { #concurrent-burgers }

你和你喜欢的人一起去吃快餐,你们排队,收银员正在给前面的人点单。😍

<img src="/img/async/concurrent-burgers/concurrent-burgers-01.png" class="illustration">

轮到你们了,你为两个人点了 2 个非常豪华的汉堡。🍔🍔

<img src="/img/async/concurrent-burgers/concurrent-burgers-02.png" class="illustration">

收银员朝厨房对厨师说了句什么,让他们知道该准备你们的汉堡了(虽然他们此刻还在做前一位客人的)。

<img src="/img/async/concurrent-burgers/concurrent-burgers-03.png" class="illustration">

你付了钱。💸

收银员给你一个取餐号。

<img src="/img/async/concurrent-burgers/concurrent-burgers-04.png" class="illustration">

等待时,你们找了一张桌子坐下,聊了很久(汉堡太豪华,做得慢)。

坐在桌边等汉堡的这段时间,你完全可以用来欣赏对方有多棒、多可爱、多聪明 ✨😍✨。

<img src="/img/async/concurrent-burgers/concurrent-burgers-05.png" class="illustration">

边聊边等,你偶尔瞄一眼柜台显示屏上的号码,看是不是轮到你们了。

终于,轮到你们了。你走到柜台取了汉堡,回到桌边。

<img src="/img/async/concurrent-burgers/concurrent-burgers-06.png" class="illustration">

你们一起吃汉堡,度过了一段美好时光。✨

<img src="/img/async/concurrent-burgers/concurrent-burgers-07.png" class="illustration">

/// note

精美插图出自 [Ketrina Thompson](https://www.instagram.com/ketrinadrawsalot) 之手。🎨

///

---

想象你就是故事里的那台计算机 / 程序 🤖。

排队时,你只是闲着 😴 等叫号,没干什么"有产出"的事。但队伍走得快,因为收银员只负责点单(不负责做汉堡),所以还好。

轮到你时,你干了真正"有产出"的活:研究菜单、决定吃什么、问对方要什么、付钱、确认递出的是对的钞票或卡、确认收款金额正确、核对订单商品无误,等等。

然后,虽然汉堡还没到手,你和收银员之间的事务进入"暂停" ⏸,因为你得等 🕙 汉堡做好。

但当你离开柜台、拿着取餐号坐到桌边,你就可以把注意力 🔀 切换到身边的人身上,在那件事上"工作" ⏯ 🤓。于是你又在做非常"有产出"的事了——和人调情 😍。

后来收银员 💁 把你们的号码放上柜台显示屏,表示"汉堡做好了",你并没有在屏幕数字一变时就疯了一样跳起来。你知道没人会抢走你们的汉堡,因为号码在你们手里。

于是你等对方把故事讲完(完成当前的工作 ⏯ / 任务 🤓),微笑着说你去拿汉堡 ⏸。

然后你走向柜台 🔀,处理那个已经完成的任务 ⏯,取汉堡、道谢、带回桌边。与柜台交互的这个步骤 / 任务就此结束 ⏹。这又创建了一个新任务:"吃汉堡" 🔀 ⏯,而之前的"取汉堡"已经完成 ⏹。

### 并行汉堡 { #parallel-burgers }

现在想象这不是"并发汉堡",而是"并行汉堡"。

你和你喜欢的人去买"并行"快餐。

你们排队,前面有好几个(假设 8 个)收银员兼任厨师同时在点单。

你前面的每个人都站在柜台前等汉堡做好才走,因为这 8 个收银员都是接到订单就立刻亲自去做汉堡,然后才接下一单。

<img src="/img/async/parallel-burgers/parallel-burgers-01.png" class="illustration">

终于轮到你们,你点了 2 个豪华汉堡,付了钱 💸。

<img src="/img/async/parallel-burgers/parallel-burgers-02.png" class="illustration">

收银员进了厨房。

你只能站在柜台前干等 🕙,因为没有取餐号,汉堡一好就得马上拿走,不能被别人抢了先。

<img src="/img/async/parallel-burgers/parallel-burgers-03.png" class="illustration">

由于你和你喜欢的人忙着守住柜台、防止汉堡被别人拿走,你根本顾不上对方。😞

这就是"同步"工作:你和收银员/厨师 👨‍🍳 是"同步"的。你必须等 🕙,而且必须恰好在收银员/厨师 👨‍🍳 做好汉堡递给你的那一刻守在那里,否则别人可能拿走它。

<img src="/img/async/parallel-burgers/parallel-burgers-04.png" class="illustration">

过了很久,你的收银员/厨师 👨‍🍳 终于拿着汉堡回来了。

<img src="/img/async/parallel-burgers/parallel-burgers-05.png" class="illustration">

你拿上汉堡,和对方回到桌边,吃完,结束。⏹

<img src="/img/async/parallel-burgers/parallel-burgers-06.png" class="illustration">

基本没聊上天,大部分时间都耗在柜台前干等 🕙 了。😞

/// note

精美插图出自 [Ketrina Thompson](https://www.instagram.com/ketrinadrawsalot) 之手。🎨

///

---

在这个并行汉堡的场景里,你是一台有两个处理器(你和你喜欢的人)的计算机 / 程序 🤖,两个处理器都在长时间 🕙 等待 🕙,把注意力 ⏯ 全放在"守在柜台前"上。

而快餐店有 8 个处理器(收银员/厨师)。刚才那家并发汉堡店可能只有 2 个(一个收银员、一个厨师)。

但最终的体验依然不佳。😞

---

这就是汉堡的"并行"版故事。🍔

一个更贴近现实的例子:银行。

直到不久前,大多数银行都是多个柜员 👨‍💼👨‍💼👨‍💼👨‍💼 加一条大长队 🕙🕙🕙🕙🕙🕙🕙🕙。

每个柜员接待完一位客户再接待下一位 👨‍💼⏯。

你得在队伍里苦等 🕙 很久,不然就失去位次。

你大概不会想带喜欢的人 😍 一起去银行 🏦 办事吧。

### 汉堡结论 { #burger-conclusion }

在"和你喜欢的人吃快餐汉堡"这个场景里,由于有大量等待 🕙,并发系统 ⏸🔀⏯ 明显更合理。

大多数 Web 应用正是这种情况。

用户很多很多,而你的服务器在等 🕙 用户那不太好的网络连接把请求发过来。

然后又要等 🕙 响应传回去。

这种"等待" 🕙 以微秒计,但加在一起,总量非常可观。

这就是为什么对 Web API 来说,使用异步 ⏸🔀⏯ 代码非常合理。

正是这种异步性成就了 NodeJS 的流行(尽管 NodeJS 并不并行),也是 Go 语言作为编程语言的强项所在。

**FastAPI** 给你的正是同等水平的性能。

而且由于你可以同时拥有并行与异步,你能获得比大多数受测 NodeJS 框架更高的性能,与 Go(一门更接近 C 的编译型语言)持平[(这一切都归功于 Starlette)](https://www.techempower.com/benchmarks/#section=data-r17&hw=ph&test=query&l=zijmkf-1)。

### 并发一定比并行好吗? { #is-concurrency-better-than-parallelism }

不!故事的重点不是这个。

并发不同于并行。在涉及大量等待的**特定**场景下,它更好。正因如此,在 Web 应用开发中它通常远胜并行。但它并非万能。

为了平衡一下,想象下面这个小故事:

> 你要打扫一栋又大又脏的房子。

*没错,故事讲完了*。

---

这里没有任何等待 🕙,只有大量的活儿要干,分布在房子的各个角落。

你可以像汉堡例子那样轮换:先客厅、再厨房。但因为你不是在等 🕙 什么,只是不停地打扫,轮换不会带来任何收益。

有没有轮换(并发),耗时都一样,干的活也一样。

但这种情况下,如果你能把那 8 位前收银员/厨师、现清洁工请来,每个人(加上你)负责房子的一个区域,你们就能**并行**干活,借助额外的人手更快完工。

在这个场景里,每个清洁工(包括你)都是一个处理器,各干各的那部分活。

由于执行时间主要花在真正的干活上(而不是等待),而计算机里的活是由 <abbr title="Central Processing Unit">CPU</abbr> 干的,这类问题被称为"CPU 密集型(CPU bound)"。

---

CPU 密集型操作的典型例子是需要复杂数学处理的工作。

例如:

* **音频**或**图像处理**。
* **计算机视觉**:一张图像由数百万像素组成,每个像素有 3 个值 / 颜色,处理它通常需要同时对所有像素进行计算。
* **机器学习**:通常需要大量的"矩阵"和"向量"乘法。想象一张巨大的数字表格,要同时把它们全部相乘。
* **深度学习**:它是机器学习的一个子领域,所以同理。只不过要相乘的不是一张数字表格,而是一大批,而且很多时候你还要用专用处理器来构建和 / 或使用这些模型。

### 并发 + 并行:Web + 机器学习 { #concurrency-parallelism-web-machine-learning }

有了 **FastAPI**,你可以利用 Web 开发中最常见的并发(NodeJS 的主要卖点正是它)。

同时,你还可以利用并行与多进程(多个进程并行运行)的优势,来处理机器学习系统这类 **CPU 密集型**负载。

再加上 Python 本身就是**数据科学**、机器学习尤其是深度学习的主力语言,这些让 FastAPI 成为数据科学 / 机器学习 Web API 和应用(以及其他众多场景)的绝佳搭档。

关于如何在生产环境实现这种并行,参见[部署](deployment/index.md)一节。

## `async` 和 `await` { #async-and-await }

现代 Python 有一套非常直观的方式来定义异步代码,让它看起来就像普通的"顺序"代码,并在恰当的时机替你完成"等待"。

某个操作需要等待才能返回结果、且支持这些新 Python 特性时,你可以这样写:

```Python
burgers = await get_burgers(2)
```

关键是 `await`。它告诉 Python:必须先等 ⏸ `get_burgers(2)` 把事情 🕙 做完,再把结果存进 `burgers`。这样 Python 就知道在等待期间可以去干别的 🔀 ⏯(比如接另一个请求)。

`await` 要生效,必须位于支持异步的函数内部。为此,只需用 `async def` 声明它:

```Python hl_lines="1"
async def get_burgers(number: int):
    # Do some asynchronous stuff to create the burgers
    return burgers
```

……而不是 `def`:

```Python hl_lines="2"
# This is not asynchronous
def get_sequential_burgers(number: int):
    # Do some sequential stuff to create the burgers
    return burgers
```

用了 `async def`,Python 就知道:这个函数内部会出现 `await` 表达式,函数的执行可以"暂停" ⏸,先去干别的 🔀,之后再回来。

调用 `async def` 函数时,你必须"await"它。所以下面这样是行不通的:

```Python
# This won't work, because get_burgers was defined with: async def
burgers = get_burgers(2)
```

---

因此,如果你使用的库要求你用 `await` 调用它,就需要用 `async def` 来创建使用它的*路径操作函数*,例如:

```Python hl_lines="2-3"
@app.get('/burgers')
async def read_burgers():
    burgers = await get_burgers(2)
    return burgers
```

### 更多技术细节 { #more-technical-details }

你可能已经注意到,`await` 只能用在 `async def` 定义的函数内部。

而另一方面,`async def` 定义的函数又必须被"await"。于是,`async def` 函数也只能在 `async def` 函数内部调用。

那么先有鸡还是先有蛋——第一个 `async` 函数怎么调用?

使用 **FastAPI** 时你完全不用操心,因为那个"第一个"函数就是你的*路径操作函数*,FastAPI 知道怎么正确处理。

不过,就算不用 FastAPI,你也可以自行使用 `async` / `await`。

### 编写你自己的异步代码 { #write-your-own-async-code }

Starlette(以及 **FastAPI**)基于 [AnyIO](https://anyio.readthedocs.io/en/stable/),因此同时兼容 Python 标准库的 [asyncio](https://docs.python.org/3/library/asyncio-task.html) 和 [Trio](https://trio.readthedocs.io/en/stable/)。

具体来说,当你的高级并发用例需要更高级的模式时,可以直接在自己的代码里使用 [AnyIO](https://anyio.readthedocs.io/en/stable/)。

即使不用 FastAPI,你也可以用 [AnyIO](https://anyio.readthedocs.io/en/stable/) 编写自己的异步应用,获得高兼容性和它的种种好处(比如*结构化并发*)。

我还在 AnyIO 之上创建了另一个库,作为一层薄封装,改进了类型注解,带来更好的**自动补全**、**内联错误提示**等。它还带有友好的入门教程,帮你**理解**并编写**自己的异步代码**:[Asyncer](https://asyncer.tiangolo.com/)。如果你需要**把异步代码与普通(阻塞/同步)代码结合**,它会特别有用。

### 其他形式的异步代码 { #other-forms-of-asynchronous-code }

这种 `async` / `await` 风格在语言中出现得相对较晚。

但它让异步代码的工作轻松了许多。

同样的语法(或几乎相同)最近也被加入了现代版 JavaScript(浏览器和 NodeJS)。

而在此之前,处理异步代码要复杂、困难得多。

在旧版 Python 中,你可以用线程或 [Gevent](https://www.gevent.org/),但代码的理解、调试和思考成本都高得多。

在旧版 NodeJS / 浏览器 JavaScript 中,你得用"回调",结果就是"回调地狱"。

## 协程 { #coroutines }

**协程(Coroutine)**只是 `async def` 函数所返回东西的一个花哨术语。Python 知道它类似函数:可以启动,终会结束,但内部也可能因 `await` 而"暂停" ⏸。

把用 `async` 和 `await` 使用异步代码的这一整套机制,常被概括为"使用协程"。可以类比 Go 的核心特性 "Goroutines"。

## 结论 { #conclusion }

再看一遍前面那句话:

> 现代 Python 支持**"异步代码"**,靠的是一种叫**"协程(coroutine)"**的机制,以及 **`async` 和 `await`** 语法。

现在应该好理解多了。✨

这一切就是 FastAPI(通过 Starlette)的动力来源,也是它性能如此惊艳的原因。

## 非常技术性的细节 { #very-technical-details }

/// warning

这一节你可以直接跳过。

以下是 **FastAPI** 底层工作原理的深度技术细节。

如果你有相当的技术功底(协程、线程、阻塞等),并且好奇 FastAPI 如何处理 `async def` 与普通 `def` 的区别,再往下读。

///

### 路径操作函数(摘译) { #path-operation-functions }

用普通 `def`(而非 `async def`)声明的*路径操作函数*会运行在外部线程池中并被 await,而不是被直接调用(直接调用会阻塞服务器)。

(细节较多,完整内容请参阅英文原版:来自其他异步框架、习惯对纯计算型函数用 `def` 换取微小性能收益的读者,请注意在 **FastAPI** 中效果恰恰相反——除非函数内有阻塞式 <abbr title="Input/Output: disk reading or writing, network communications.">I/O</abbr>,否则建议用 `async def`。)

### 依赖项(摘译) { #dependencies }

同样的规则适用于[依赖项](tutorial/dependencies/index.md):普通 `def` 依赖会运行在外部线程池。[子依赖](tutorial/dependencies/sub-dependencies.md)之间 `async def` 与普通 `def` 可以混用,依然正常工作。

### 其他工具函数(摘译) { #other-utility-functions }

你自己直接调用的工具函数,用 `def` 或 `async def` 都可以,FastAPI 不会改变你的调用方式。这与 FastAPI 替你调用的函数(*路径操作函数*和依赖项)不同。

---

总之,这些细节只对专门来找它们的人有用。否则,遵循上一节"[赶时间?](#in-a-hurry)"的指引就够了。
