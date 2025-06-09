from flask import Flask, request, render_template_string

app = Flask(__name__)

# Simple chatbot function
def simple_chatbot(user_query):
    user_query = user_query.lower()  # Convert user input to lowercase
    
    if user_query == "what is npk fertilizer?":
        return "npk stands for nitrogen (n), phosphorus (p), and potassium (k), the three primary nutrients plants need."
    elif user_query == "when should i apply nitrogen fertilizer?":
        return "apply nitrogen fertilizer at the early growth stages when the plant is growing leaves."
    elif user_query == "what is the ideal npk ratio for wheat?":
        return "120:60:40 (kg/ha) of n, p, and k is recommended for wheat."
    elif user_query == "can i apply too much fertilizer?":
        return "yes, over-fertilization can damage plants, reduce yield, and harm the soil."
    elif user_query == "how often should i apply fertilizer to my crops?":
        return "it depends on the crop; usually once during planting and once in the growing stage."
    elif user_query == "what is the best fertilizer for rice?":
        return "use an npk ratio of 120:60:40 and apply during the vegetative growth stage."
    elif user_query == "what fertilizer is best for maize?":
        return "a balanced npk ratio of 120:60:60 is ideal for maize crops."
    elif user_query == "when should i fertilize my tomato plants?":
        return "fertilize tomatoes with nitrogen during early growth, then switch to a phosphorus-heavy fertilizer before fruiting."
    elif user_query == "how much potassium is required for potato cultivation?":
        return "about 150 kg of potassium per hectare is recommended for potato crops."
    elif user_query == "what fertilizer should i use for sugarcane?":
        return "an npk ratio of 180:90:120 (kg/ha) is recommended for sugarcane."
    else:
        return "sorry, i can only provide information on predefined queries."


# Enhanced HTML template for PC-like design
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BHOOGAMINI</title>
    <!-- Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background:#fff ;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
        }
        .chat-container {
            width: 70%; /* Adjust width to make it more desktop-friendly */
            max-width: 900px;
            height: 80vh;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }
        .chat-header {
            background-color: #007bff;
            padding: 20px;
            color: white;
            text-align: center;
            font-size: 1.5rem;
            font-weight: bold;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
        }
        .chat-body {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            background-color: #f1f1f1;
            border-bottom: 2px solid #007bff;
        }
        .chat-bubble {
            max-width: 60%;
            padding: 10px 15px;
            border-radius: 20px;
            margin-bottom: 15px;
            font-size: 1rem;
            position: relative;
            margin-left: 20px;
            margin-right: 20px;
        }
        .chat-bubble.user {
            align-self: flex-end;
            background-color: #007bff;
            color: white;
        }
        .chat-bubble.bot {
            align-self: flex-start;
            background-color: #e9ecef;
            color: #343a40;
        }
        .chat-bubble::after {
            content: "";
            position: absolute;
            bottom: 0;
            width: 0;
            height: 0;
            border-style: solid;
        }
        .chat-bubble.user::after {
            right: -10px;
            border-width: 10px 0 10px 10px;
            border-color: transparent transparent transparent #007bff;
        }
        .chat-bubble.bot::after {
            left: -10px;
            border-width: 10px 10px 10px 0;
            border-color: transparent #e9ecef transparent transparent;
        }
        .chat-footer {
            padding: 15px;
            background-color: #f8f9fa;
            display: flex;
            align-items: center;
            border-bottom-left-radius: 10px;
            border-bottom-right-radius: 10px;
        }
        .chat-footer input {
            flex: 1;
            padding: 10px;
            border-radius: 50px;
            border: 1px solid #ced4da;
            margin-right: 10px;
        }
        .chat-footer button {
            background-color: #007bff;
            border: none;
            color: white;
            padding: 10px 15px;
            border-radius: 50px;
            cursor: pointer;
            font-weight: bold;
        }
        .chat-footer button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>

<div class="chat-container">
    <div class="chat-header">
        BHOOGAMINI
    </div>
    <div class="chat-body" id="chat-body">
        {% for message in messages %}
            <div class="chat-bubble {{ message.sender }}">
                {{ message.text }}
            </div>
        {% endfor %}
    </div>
    <div class="chat-footer">
        <form action="/" method="POST" style="display: flex; width: 100%;">
            <input type="text" class="form-control" id="query" name="query" placeholder="Type your question..." autocomplete="off">
            <button type="submit">Send</button>
        </form>
    </div>
</div>

<!-- Automatically scroll to the bottom of the chat body -->
<script>
    document.getElementById('chat-body').scrollTop = document.getElementById('chat-body').scrollHeight;
</script>

<!-- Bootstrap JS and dependencies -->
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.1/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

</body>
</html>
'''

# Route for the home page
@app.route("/", methods=["GET", "POST"])
def home():
    messages = []
    if request.method == "POST":
        user_query = request.form.get("query")
        bot_response = simple_chatbot(user_query)
        messages.append({"sender": "user", "text": user_query})
        messages.append({"sender": "bot", "text": bot_response})
    return render_template_string(html_template, messages=messages)

# Run the Flask app
if __name__ == "__main__":
    app.run(port=5001)
