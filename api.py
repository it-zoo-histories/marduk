from flask import Flask, request, jsonify
from entry import LogicCore

app = Flask(__name__)
coreLogic = LogicCore()

@app.route("/", methods=["POST"])
def startConversation():
    message = request.get_json()
    coreLogic.interpreter(message['message'])

    result = coreLogic.newMessage(message['message'])
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run()
