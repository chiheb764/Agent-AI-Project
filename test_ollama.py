
import requests
def llm_local(prompt):
    url = (
    "http://localhost:11434/api/generate"
    )
    data = {
    "model": "phi3",
    "prompt": prompt,
    "stream": False
    }
    response = requests.post(
    url,
    json=data
    )
    return response.json()["response"]
url = (
"http://localhost:11434/api/generate"
)
data = {
"model": "phi3",
"prompt": "Bonjour",
"stream": False
}
response = requests.post(
url,
json=data
)
print(
response.json()
)
