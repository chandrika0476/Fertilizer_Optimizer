import google.generativeai as genai
from flask import Flask, render_template, request

# Initialize the Flask app
app = Flask(__name__)

# Set your API key here
api_key = 'write your key here'

# Initialize the Gemini model with your API key
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        try:
            response = model.generate_content(user_input)
            return render_template("index.html", user_input=user_input, response=response.text)
        except Exception as e:
            return render_template("index.html", error="Error: " + str(e))
    return render_template("index.html", response=None)

if __name__ == "__main__":
    app.run(debug=True,port=5001)


