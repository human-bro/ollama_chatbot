from flask import Flask, render_template, request
import ollama
import json
from datetime import datetime

app = Flask(__name__)

# Define the path for the chat history file
CHAT_HISTORY_FILE = 'chat.json'

def read_chat_history():
    """Read chat history from the JSON file."""
    try:
        with open(CHAT_HISTORY_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def write_chat_history(chat_history):
    """Write the chat history back to the JSON file."""
    with open(CHAT_HISTORY_FILE, 'w') as f:
        json.dump(chat_history, f, indent=4)

@app.route('/', methods=['GET', 'POST'])
def chat():
    model_name = 'llama3.2'
    
    # Load existing chat history
    chat_history = read_chat_history()
    response_message = ""

    if request.method == 'POST':
        user_input = request.form['user_input']

        # Get the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Get AI response from Ollama
        response = ollama.chat(model=model_name, messages=[
            {
                'role': 'user',
                'content': user_input,
            },
        ])
        response_message = response['message']['content']
        
        # Store user input and AI response with the current timestamp
        chat_history[timestamp] = {
            'user_input': user_input,
            'ai_response': response_message
        }

        # Write updated chat history back to the file
        write_chat_history(chat_history)

    # Prepare chat history for rendering in the template
    sorted_chat_history = sorted(chat_history.items(), key=lambda x: x[0])

    return render_template('index.html', response=response_message, chat_history=sorted_chat_history)

if __name__ == '__main__':
    app.run(debug=True)
