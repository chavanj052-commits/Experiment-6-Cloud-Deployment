from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Experiment 6</title>
    </head>
    <body style="text-align:center; font-family:Arial;">
        <h1>Welcome to Cloud Computing!</h1>
        <h2>Google App Engine Alternative Using Render</h2>
        <p>My Python Flask application is successfully deployed.</p>
        <p>Experiment No. 6</p>
        <p>Cloud Platform: Render</p>
    </body>
    </html>
    """

@app.route('/about')
def about():
    return "This application is developed using Python Flask."

if __name__ == '__main__':
    app.run(debug=True)