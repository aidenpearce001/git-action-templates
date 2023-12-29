from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/redirect')
def unsafe_redirect():
    url = request.args.get('url')  # Untrusted input for redirection
    return redirect(url)  # Insecure