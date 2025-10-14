# test_prompt.py
import json, sys

try:
    import requests
except ImportError:
    print("Instala la librería requests: pip install requests")
    sys.exit(1)

url = "http://10.5.0.2:1234/v1/chat/completions"
headers = {"Content-Type": "application/json"}   # Añade Authorization si tu servidor lo necesita

payload = {
    "model": "gpt-oss",
    "messages": [
        {"role": "user", "content": "Hola, ¿cómo estás?"}
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

print("Status:", response.status_code)
print("Respuesta JSON:")
print(response.json())
