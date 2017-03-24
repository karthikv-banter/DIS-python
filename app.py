from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

callers = {}

@app.route("/", methods=['GET', 'POST'])
def dis_handler():
    """Respond to incoming SMS."""

    from_number = request.values.get('From', None)
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "Monkey, thanks for the message!"

    resp = twilio.twiml.Response()
    resp.message(message)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
