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
2. Start registrar: ``` python service_registrar.py ```
3. Start two services:

   
   ```
   python ollama_microservice.py service_a 5001
   python ollama_microservice.py service_b 5002
   ```
## Sample Response

   ![image_2025-02-15_21-46-02](https://github.com/user-attachments/assets/f7671db8-aad4-4a9f-86be-99df9361419b)

![image_2025-02-15_21-46-31](https://github.com/user-attachments/assets/4d93627f-2a0c-402c-8027-b93fea3dfa0d)
