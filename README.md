# Service Discovery

Service Discovery is a mechanism in a microservices architecture that allows services to register their network locations (e.g., IP addresses, ports) and enables other services to locate and communicate with them dynamically. This helps avoid hard-coded endpoints and supports scalability and resilience in distributed systems. 

In this project we have used self service registration process.

---

##  Tech Stack

- Ollama (Locally installed LLM)
- Python (Backend development)
- Flask (Microservice framework)
- REST API (For communication)

---

# Installation & Setup for Windows

## Install [Ollama Locally](https://ollama.com/download/OllamaSetup.exe), [Python](https://www.python.org/downloads/), [VS Code](https://code.visualstudio.com/download), [Postman](https://www.postman.com/downloads/)

## Clone This Repository


git clone https://github.com/NilayPatel27/serviceDiscovery

# Testing the API in Postman
1. Start Ollama server: ``` ollama serve ```
2. Start registrar on machine 1: ``` python service_registrar.py ```
3. Enter below code in the terminal to start the services in machine 1 and machine 2 respectively:

```sh
python ollama_microservice.py service_a 6000
```

```sh
python ollama_microservice.py service_b 6000
```

4. To see all the services running enter below code in postman:
   ```sh
   curl --location 'http://<ServiceDiscovery_IP>:5000/services'
   ```
5. To forward a message enter below code in postman:
    ```sh
   curl --location 'http://<ServiceDiscovery_IP>:5000/forward' \
   --header 'Content-Type: application/json' \
   --data '{
     "from": "service_a",
     "to": "service_b",
     "prompt": "What'\''s the chatgpt?"
   }'
   ```
