# LLM Service Testing demo code

Welcome to the **LLM Service Testing demo code**! This repository contains all the necessary code and tools to test generative language model (LLM) services efficiently and in a structured manner. Whether you're evaluating LLM capabilities, integrating with third-party APIs, or building your own custom use cases, this repository will help you get started.

## Usage

1. with API Key

```shell
python test_gpt_api.py
    --url=https://api.openai.com/v1/chat/completions \
    --model=gpt-4o \
    --api-key="YOUR_API_KEY" \
    --sys-prompt="default system context" \
    --usr-prompt="hello world"
```

2. without API Key

```shell
python test_gpt_api.py
    --url=YOUR_ENDPOINT_URL_LINK_HERE \
    --model=gpt-4o \
    --sys-prompt="default system context" \
    --usr-prompt="hello world"
```

## From curl

1. with API Key

```shell
curl https://api.openai.com/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
        "model": "gpt-4o",
        "messages": [
        {
            "role": "user",
            "content": "Hello!"
        }
        ]
    }'

```

2. without API Key

```shell
curl -X POST "YOUR_ENDPOINT_URL_LINK_HERE" \
    -H "Content-Type: application/json" \
    -d '{
        "messages": [
            {
            "role": "user", "content": "Hello"
            }
        ],
        "model": "gpt-4o"
    }'
```
