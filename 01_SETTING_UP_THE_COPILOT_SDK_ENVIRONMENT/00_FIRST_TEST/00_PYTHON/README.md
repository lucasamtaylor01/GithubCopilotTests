# Python Examples - Copilot SDK

This directory contains Python examples demonstrating how to use the GitHub Copilot SDK with async/await patterns.

## 🚀 Quick Start

```bash
pip install -r requirements.txt
python first_agent.py
```

## Files

- **first_agent.py** - Main example showing:
  - Async Copilot client initialization
  - Event handling for assistant messages
  - Session management
  - Understanding async/await with asyncio

- **101_examples/** - Basic educational examples:
  - `asyncio_example.py` - Asyncio basics
  - `partial_example.py` - functools.partial usage

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up your Copilot SDK environment (authentication required)

## Running Examples

```bash
python first_agent.py
```

## Running Educational Examples

```bash
# Learn asyncio basics
python 101_examples/asyncio_example.py

# Learn functools.partial
python 101_examples/partial_example.py
```

## Key Concepts

- **async/await**: Demonstrates coroutines and event loop usage
- **Event Handling**: Shows how to handle Copilot service events
- **Session Management**: Creates and manages Copilot client sessions
