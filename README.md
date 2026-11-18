# Breakfast Ideas: Prompt Formatting with LangChain

> A first LangChain script that shows how precise instructions control LLM output format.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white) ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?logo=langchain&logoColor=white) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?logo=openai&logoColor=white) ![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

## Overview

A short starter project: one prompt asks `gpt-4o-mini` for **exactly 5** healthy breakfast ideas, numbered, one line each, with no extra text. It demonstrates how clear formatting constraints make LLM output predictable enough to use in code.

## Demo

![Example run](Screenshot_breakfast.png)

## Tech stack

| Layer | Technology |
|---|---|
| Orchestration | LangChain |
| Model | OpenAI `gpt-4o-mini` |

## Project structure

```text
.
├── breakfast.py
├── requirements.txt
└── .env.example
```

## Getting started

**Prerequisites:** Python 3.10+

```bash
git clone https://github.com/prasanth-sundararajan/breakfast.git
cd breakfast
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your keys:

```bash
cp .env.example .env
```

## Usage

```bash
python breakfast.py
```

## Configuration

| Variable | Required | Description |
|---|---|---|
| `OPENAI_API_KEY` | Yes | OpenAI API key used for chat and embeddings |

## License

Released under the [MIT License](LICENSE).

## Author

**Prasanth Sundararajan**, Senior SRE and AI Engineer  
[LinkedIn](https://www.linkedin.com/in/prasanth-s-a093a7109/) · [GitHub](https://github.com/prasanth-sundararajan)
