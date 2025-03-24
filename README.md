# Feedly MCP

[![CI](https://github.com/ShaojieJiang/feedly-mcp/actions/workflows/ci.yml/badge.svg?event=push)](https://github.com/ShaojieJiang/feedly-mcp/actions/workflows/ci.yml?query=branch%3Amain)
[![Coverage](https://coverage-badge.samuelcolvin.workers.dev/ShaojieJiang/feedly-mcp.svg)](https://coverage-badge.samuelcolvin.workers.dev/redirect/ShaojieJiang/feedly-mcp)
[![PyPI](https://img.shields.io/pypi/v/feedly-mcp.svg)](https://pypi.python.org/pypi/feedly-mcp)

A MCP for Feedly.

Core functionality:
- Get the latest entries from a category.
- Mark an entry as read.

## Workflow

```mermaid
flowchart TD
  A([Start]) --> B[Get latest entries]
  B --> C[Check each entry]
  C --> D{Is entry interesting?}
  D -->|No| E[Mark as read]
  D -->|Yes| F[Keep unread]
  E --> G{All entries checked?}
  F --> G
  G -->|Yes| H([End])
  G -->|No| C
```

