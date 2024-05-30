from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_bot_response(user_input)
    return jsonify({"response": response})


def get_bot_response(user_input):
    a = user_input.lower()
    a = user_input.split()
    if 'hello' in a or 'hi':
        return 'Hi how can i assist you..! '
    elif 'how' in a and 'you' in a:
        return 'I am good, thank you!'
    else:
        return 'Sorry can you specify that.'


if __name__ == '__main__':
    app.run(debug=True)