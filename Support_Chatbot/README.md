# README Documentation for Flask-Azure Chatbot Application

## Overview
This Flask application is designed to interact with Azure's cognitive services, particularly utilizing Azure's version of OpenAI for a chat interface. It integrates Flask web framework for backend operations and leverages Azure's Search Client for querying a database. The app responds to user questions by searching an Azure-hosted database and processing the results through a language model.

## Features
- REST API endpoint to receive and process messages.
- Integration with Azure's version of OpenAI for chat responses.
- Search functionality using Azure's Search Client.
- Environmental variables for secure configuration.

## Prerequisites
- Python 3
- Flask
- Azure account and relevant Azure services configured (Search Services, Cognitive Services).
- `.env` file with necessary Azure configuration keys.

## Installation
1. Clone the repository.
2. Install required Python packages: `pip install flask python-dotenv azure-search-documents langchain_community`.
3. Ensure you have an `.env` file with Azure configuration details (API keys, endpoints).

## Usage
1. Start the server with `python <filename>.py`.
2. The server runs on `http://localhost:5000/` and listens for POST requests at `/sendMessageToAzure`.
3. Send a POST request with a JSON body containing a "Question" key.
4. The application processes the question, searches the Azure-hosted database, and returns a response.

## Application Flow
1. **Initialization**: Flask app and CORS are set up. The Azure chat model and search client are configured using environment variables.
2. **API Endpoint (`/sendMessageToAzure`)**: Listens for POST requests. Extracts the question from the request body.
3. **Question Processing**:
   - The AzureChatOpenAI model is prepared with the necessary API keys and endpoints.
   - The SearchClient is configured for database querying.
   - The received question is passed to the Azure search component and language model chain.
4. **Response Generation**:
   - The application searches the database for relevant information.
   - The language model generates a response based on the search results and the question.
   - The response is returned as JSON.

## Environment Variables
The application requires the following environment variables:
- `AZURE_OPENAI_ENDPOINT`: Endpoint for Azure's OpenAI service.
- `AZURE_OPENAI_DEPLOYMENT_NAME`: Deployment name for the Azure OpenAI service.
- `AZURE_OPENAI_KEY`: API key for Azure's OpenAI service.
- `SEARCH_SERVICE_NAME`: Name of the Azure search service.
- `SEARCH_INDEX_NAME`: Name of the search index in Azure search service.
- `SEARCH_API_KEY`: API key for the Azure search service.

## Error Handling
- The application returns a 200 HTTP status code for successful responses and 401 for unauthorized or bad requests.

## Security
- Ensure that the `.env` file containing sensitive keys is properly secured and not included in version control.

## Limitations
- The search is currently limited to the top 3 results from the Azure database.
- The language model's capabilities are dependent on the Azure OpenAI API version and configuration.

## Future Improvements
- Expand the search result handling for more comprehensive coverage.
- Implement additional security measures for API access.
- Enhance the language model's response accuracy and detail.

## Support

- For issues and queries regarding the application or its deployment, contact me on Teams dominik.dierberger@futurelog.com :3😺🐈
---
