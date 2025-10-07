import os
from dotenv import load_dotenv
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from langchain_community.chat_models import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

app = Flask(__name__)
CORS(app)


@app.route('/sendMessageToAzure', methods=['POST'])
def sendAndReceiveMessage():
    question = ''
    response_content = ''
    load_dotenv()

    if request.method == 'POST':
        data = request.get_json()
        question = data["Question"]

        model = AzureChatOpenAI(
            openai_api_type="azure",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            openai_api_version='2023-03-15-preview',
            deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            api_key=os.getenv("AZURE_OPENAI_KEY")
        )

        search_service_name = os.getenv("SEARCH_SERVICE_NAME")
        search_index_name = os.getenv("SEARCH_INDEX_NAME")
        search_api_key = os.getenv("SEARCH_API_KEY")

        search_client = SearchClient(
            endpoint=f"https://{search_service_name}.search.windows.net/",
            index_name=search_index_name,
            credential=AzureKeyCredential(search_api_key)
        )

        def search_database(query):
            results = search_client.search(search_text=query)
            return [result for result in results]

        def format_search_results(results):
            if not results:
                return "I couldn't find any information on that topic."
            formatted_results = "Here's what I found: "
            for result in results[:3]:
                formatted_results += f"\n- {result['content']}"
            return formatted_results

        def azure_search_component(query):
            return format_search_results(search_database(query))

        prompt_answer = f"""You are a helpful assistant that can answer questions related to the webapp FutureLog.
        Answer the question based on the given documentation below. Your answer must be concise. You can also answer without the Documentation if the Information isn't found in your files. Please just tell the user so.

        Documentation: {{search_results}}

        Question: {{question}}
        Answer: """

        chain_answer = LLMChain(llm=model, prompt=PromptTemplate.from_template(prompt_answer))
        answer = chain_answer.run({
            'search_results': azure_search_component(question),
            'question': question
        })

        return jsonify({"message": answer}), 200
    else:
        return jsonify({"message": "bad"}), 401


if __name__ == '__main__':
    app.run(debug=True)
