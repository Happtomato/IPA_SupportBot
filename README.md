
# IPA Support Chatbot

This project was developed as part of my final Individual Practical Assignment (IPA) to successfully complete my apprenticeship as a software developer. It serves as a demonstration of applied skills in full-stack development, cloud services, and AI integration.

The **IPA Support Chatbot** is an AI-powered assistant designed to help users find answers to product-related questions using a natural language interface. It integrates a modern Svelte-based frontend with a Python Flask backend and utilizes Microsoft Azure services such as OpenAI and AI Search for intelligent response generation.

---

## 📌 Project Structure


```html
IPA/
├── svelte-support-frontend/                    # Svelte frontend with chat interface  
├── Support_Chatbot/                            # Python Flask backend with Azure OpenAI + Search integration  
├── DominikDierberger-IPA-Dokumentation.pdf     # Full technical project documentation  
└── README.md                                   # This file  
```
---

## 🔍 Project Overview

**Goal:**  
The chatbot provides users with fast, AI-assisted answers to support-related questions, by combining:  
- User-friendly chat UI (via Svelte frontend)  
- Flask backend that connects to:  
  - Azure OpenAI for response generation  
  - Azure AI Search for knowledge retrieval  

**Use Case:**  
Originally designed for a supplier in the food logistics sector, this chatbot is tailored to search and answer from a structured product information base.

---

## 🧱 Technologies Used

| Layer       | Technology                                                                                                 |
|-------------|------------------------------------------------------------------------------------------------------------|
| Frontend    | [Svelte](https://svelte.dev/), HTML/CSS                                                                    |
| Backend     | [Flask](https://flask.palletsprojects.com/), Python                                                        |
| AI & Search | [Azure OpenAI](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/), Azure Cognitive Search |
| Hosting     | [Azure Web App](https://azure.microsoft.com/en-us/products/app-service/), Azure Function                   |
| DevOps      | Docker, Git                                                                                                |

---

## 🧠 Architecture Overview

- **Frontend** (`svelte-support-frontend`)  
  - Svelte-based SPA (Single Page Application)  
  - Chat interface to input questions and view responses  
  - Communicates with backend via HTTP requests  
  - Dockerized for portable deployment  

- **Backend** (`Support_Chatbot`)  
  - Flask API handling incoming chat messages  
  - Uses Azure AI Search to find relevant documents  
  - Generates contextual replies using Azure OpenAI  
  - Returns response to frontend  

- **Azure Integration**  
  - Azure AI Search Index stores product information  
  - Azure OpenAI GPT deployment generates human-like replies  
  - .env file used to manage all secrets and keys securely  

---

## 🚀 Getting Started

Each component has its own setup instructions. Refer to:

- [`svelte-support-frontend/README.md`](./svelte-support-frontend/README.md) → for frontend usage and Docker deployment  
- [`Support_Chatbot/README.md`](./Support_Chatbot/README.md) → for backend setup and Azure configuration  

In short:

### Frontend
```bash
cd svelte-support-frontend
npm install
npm run dev
# or via Docker:
docker-compose up --build
```

### Backend
```bash
cd Support_Chatbot
pip install -r requirements.txt
python app.py
```

Make sure to configure the .env file in the backend with your Azure API keys and endpoints.

---

📄 Full Documentation

For detailed explanation, design decisions, screenshots, and evaluation of the entire system, refer to the full project documentation:

📎 DominikDierberger-IPA-Dokumentation.pdf

This PDF includes:  
- Initial problem analysis  
- Architecture diagrams  
- Code explanations  
- Evaluation & potential improvements  

---

👨‍💻 Authors  
- Dominik Dierberger  
- [IPA Final Project – 2025]  

---

🏁 Status

✅ Completed as part of the final IPA project in Spring 2024.  
☁️ Ready for deployment via Docker or Azure Cloud.  

---

📬 Contact

For questions regarding this project, please refer to the documentation PDF or reach out to the project authors.
