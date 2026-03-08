from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    
    response = requests.get(url)
    data = response.json()

    fact = data["text"]

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Useless Info</title>
    </head>
    <body style="text-align:center; margin-top:100px; font-family:Arial;">
        <h1>🤓 Random Useless Fact</h1>
        <p style="font-size:20px;">{fact}</p>
        <br>
        <button onclick="window.location.reload()">Get Another Fact</button>
    </body>
    </html>
    """

    return render_template_string(html)


if __name__ == '__main__':
    app.run(debug=True)