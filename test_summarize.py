import requests

url = "http://127.0.0.1:8001/summarize"
data = {
    "text": "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. The key features are fast to code, fewer bugs, and easy integration with OpenAPI.",
    "max_length": 30
}
response = requests.post(url, json=data)
print("Summary:", response.json())
