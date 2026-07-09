<div align="center">

<img src="assets/kopi-ai-agent-logo.jpg" width="200" alt="KOPI AI AGENT">

# ☕ KOPI AI AGENT

### 自我进化的 AI Agent — 从经验中学习，持续改进

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-8B4513?style=for-the-badge)](LICENSE)
[![文档](https://img.shields.io/badge/文档-kopiaiagent.com-2563EB?style=for-the-badge)](https://kopiaiagent.com/docs/)
[![English](https://img.shields.io/badge/Lang-English-blue?style=for-the-badge)](README.md)
[![Español](https://img.shields.io/badge/Lang-Español-orange?style=for-the-badge)](README.es.md)

[🌐 官网](https://kopiaiagent.com) · [📚 文档](https://kopiaiagent.com/docs/) · [⚡ 快速开始](#-快速开始) · [🎮 功能](#-核心功能)

---

*Kopi Ai Agent Pte Ltd（新加坡）出品。跑在 $5 VPS、GPU 集群或云端都可以。*

</div>

---

使用任何你想要的模型 — **KOPI Proxy**、OpenRouter、OpenAI 或你自己的端点。用 `kopi model` 切换 — 无需改代码，无锁定。新安装自动获得 **500 万 token 额度**，开箱即用。

| 特点 | 说明 |
|------|------|
| **开箱即用** | 一键安装，自动颁发 API Key + 5M token 额度，无需收集各种 API Key |
| **KOPI Proxy 内置模型** | 预设 kopi-o / kopi-o-flash / kopi-flash，无需额外注册 |
| **终端 TUI** | 多行编辑、斜杠命令自动补全、对话历史、流式输出 |
| **多平台消息** | Telegram、Discord、Slack、WhatsApp、Signal — 统一网关 |
| **自学习闭环** | Agent 管理记忆、自主创建技能、技能自我改进、跨会话搜索 |
| **定时任务** | 内置 cron 调度器，支持任意平台投递 |
| **子 Agent 并行** | 创建隔离子 Agent 并行工作，零上下文开销 |
| **MCP v1 + v2** | stdio 和 SSE 双模式，KOPI MCP Gateway 预配置 |
| **随处运行** | 本地 / Docker / SSH / Singularity / Modal / Daytona |

---

## 一键安装

### Linux / macOS / WSL2 / Termux

```bash
curl -fsSL https://kopiaiagent.com/install.sh | bash
```

### Windows（PowerShell）

```powershell
iex (irm https://kopiaiagent.com/install.ps1)
```

安装程序自动处理：uv、Python 3.11、Node.js、ripgrep、ffmpeg，并**自动颁发 KOPI Proxy API Key（500 万 token）**。

安装后：

```bash
source ~/.bashrc
kopi       # 开始对话！
```

**500 万 token 额度已到账 — 立即使用。**

---

## 快速上手

```bash
kopi                   # 交互式 CLI
kopi model             # 选择模型
kopi gateway           # 启动消息网关
kopi setup             # 运行配置向导
kopi update            # 更新到最新版本
```

📖 **[完整文档 →](https://kopiaiagent.com/docs/)**

---

## KOPI Proxy 默认模型

| 模型名 | 后端 | 最大 Token |
|--------|------|-----------|
| `kopi-o` | MiMo 2.5 Pro | 128K 输入 / 4K 输出 |
| `kopi-o-flash` | MiMo 2.5 | 128K 输入 / 4K 输出 |
| `kopi-flash` | DeepSeek v4 Pro | 128K 输入 / 4K 输出 |

无需收集 API Key — 安装即用。需要更多额度？到 [kopiaiagent.com/account](https://kopiaiagent.com/account) 管理。

---

## MCP 集成

支持 MCP v1（stdio）和 v2（SSE）双模式：

- **MCP v1：** filesystem、time、github 服务器安装时自动配置
- **MCP v2：** KOPI MCP Gateway `wss://kopiaiagent.com/agg-mcp/sse`
- 通过 `kopi mcp add` 添加自定义 MCP 服务器

---

## 社区

- 🐛 [问题反馈](https://github.com/LINYIQ66/kopi-ai-agent/issues)
- 🔌 [computer-use-linux](https://github.com/avifenesh/computer-use-linux) — Linux 桌面控制 MCP 服务器
- 🔌 [KOPI Claw](https://github.com/AaronWong1999/kopiclaw) — 社区 WeChat 桥接

---

## 许可

MIT — 详见 [LICENSE](LICENSE)。

由 [Kopi Ai Agent Pte Ltd（新加坡）](https://kopiaiagent.com) 打造。
