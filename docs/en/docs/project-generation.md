> 🌐 本文档由 [fastapi/fastapi](https://github.com/fastapi/fastapi) 翻译,英文原版见原项目。

# 全栈 FastAPI 模板 { #full-stack-fastapi-template }

模板虽然通常自带一套特定配置,但其设计目标是灵活、可定制。你可以修改和调整它以满足项目需求,因此它是非常好的起点。🏁

你可以直接用这个模板起步,它已经替你完成了大量初始配置、安全设置、数据库以及一些 API 端点。

GitHub 仓库:[Full Stack FastAPI Template](https://github.com/fastapi/full-stack-fastapi-template)

## 全栈 FastAPI 模板 - 技术栈与特性 { #full-stack-fastapi-template-technology-stack-and-features }

- ⚡ [**FastAPI**](https://fastapi.tiangolo.com) 作为 Python 后端 API。
  - 🧰 [SQLModel](https://sqlmodel.tiangolo.com) 负责 Python 与 SQL 数据库的交互(ORM)。
  - 🔍 [Pydantic](https://pydantic.dev/docs/)(FastAPI 所使用)负责数据校验和配置管理。
  - 💾 [PostgreSQL](https://www.postgresql.org) 作为 SQL 数据库。
- 🚀 [React](https://react.dev) 作为前端。
  - 💃 使用 TypeScript、hooks、Vite 等现代前端技术栈。
  - 🎨 [Tailwind CSS](https://tailwindcss.com) 和 [shadcn/ui](https://ui.shadcn.com) 构建前端组件。
  - 🤖 自动生成的前端客户端。
  - 🧪 [Playwright](https://playwright.dev) 做端到端测试。
  - 🦇 支持暗色模式。
- 🐋 [Docker Compose](https://www.docker.com) 覆盖开发与生产环境。
- 🔒 默认安全的密码哈希。
- 🔑 JWT(JSON Web Token)认证。
- 📫 基于邮件的密码找回。
- ✅ 使用 [Pytest](https://pytest.org) 的测试。
- 📞 [Traefik](https://traefik.io) 作为反向代理 / 负载均衡器。
- 🚢 基于 Docker Compose 的部署说明,包括如何配置前端 Traefik 代理来自动处理 HTTPS 证书。
- 🏭 基于 GitHub Actions 的 CI(持续集成)与 CD(持续部署)。
