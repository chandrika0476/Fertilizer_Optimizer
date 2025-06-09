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

# Updated HTML and CSS template
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chatbot</title>
  <style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
}
body {
    background: #fff;
}
.chatbot-toggler {
    position: fixed;
    right: 40px;
    bottom: 35px;
    height: 50px;
    width: 50px;  
    color: #fff;
    border: none;
    display: flex;
    align-items: center;
    justify-content: center;
    outline: none;
    cursor: pointer;
    background: #2dd15c;
    border-radius: 50%;
}
.chatbot-toggler span {
    position: absolute;
}
.show-chatbot .chatbot-toggler span:first-child,
.chatbot-toggler span:last-child {
    opacity: 0;
}
.show-chatbot .chatbot-toggler span:last-child{
    opacity: 1;

}
.Chatbot{
    position: fixed;
    right: 40px;
    bottom: 100px;
    width: 420px;
    transform: scale(0.5);
    opacity: 0;
    pointer-events: none;
    overflow: hidden;
    background: #fff;
    border-radius: 15px;
    box-shadow: 0 0 128px 0 rgba(0,0,0,0.1),
                0 32px 64px -48px rgba(0,0,0,0.5)
}
.show-chatbot .chatbot {
    transform: scale(1);
    opacity: 1;
    pointer-events: auto;
}
.chatbot header{
    background: #2dd15c;
    padding: 16px 0;
    text-align: center;
}
.chatbot header h2{
    color: #fff;
    font-size: 1.4rem;
}
.chatbot .chatbox {
    height: 510px;
    overflow-y: auto;
    padding: 30px 20px 70px;
}
.chatbox .chat {
    display: flex;

}
.chatbox .incoming span {
    height: 32px;
    width: 32px;
    color: #fff;
    align-self: flex-end;
    background: #2dd15c;
    text-align: center;
    line-height: 32px;
    border-radius: 4px;
    margin: 0 10px 7px 0;
}
.chatbox .outgoing {
    justify-content: flex-end;
    margin: 20px 0;
}
.chatbox .chat p{
    color: #fff;
    max-width: 75%;
    font-size: 0.95rem;
    padding: 12px 16px;
    border-radius: 10px 10px 0 10px;
    background: #2dd15c;
}
.chatbox .incoming p {
    color: #000;
    background: #f2f2f2;
    border-radius: 10px 10px 10px 0;
}
.chatbot .chat-input {
    position: absolute;
    bottom: 0;
    width: 100%;
    display: flex;
    gap: 5px;
    background: #fff;
    padding: 5px 20px;
    border-top: 1px solid #ccc; 
}
.chat-input textarea {
    height: 55px;
    width: 100%;
    border: none;
    outline: none;
    font-size: 0.95rem;
    resize: none;
    padding: 16px 15px 16px 0;
}
.chat-input span{
    align-self: flex-end;
    height: 55px;
    line-height: 55px;
    color: #2dd15c;
    font-size: 1.35rem; 
    cursor: pointer;
    visibility: hidden;
}

.chat-input textarea:valid ~ span {
    visibility: visible;
}
</style>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0">
</head>
<body class="show-chatbot">
 
  <div class="chatbot">
    <header>
      <h2>Bhoogamini</h2>
    </header>
    <ul class="chatbox">
      {% for message in messages %}
      <li class="chat {% if message.sender == 'user' %}outgoing{% else %}incoming{% endif %}">
        <span class="material-symbols-outlined">smart_toy</span>
        <p>{{ message.text }}</p>
      </li>
      {% endfor %}
    </ul>
    <div class="chat-input">
      <form action="/" method="POST" style="display: flex; width: 100%;">
        <textarea id="query" name="query" placeholder="Enter a message..." required></textarea>
        <span onclick="document.querySelector('form').submit();" class="material-symbols-outlined">send</span>
      </form>
    </div>
  </div>
</body>
</html>
'''

# Route for the home page
@app.route("/", methods=["GET", "POST"])
def home():
    messages = [{"sender": "bot", "text": "Hi there 👋 How can I help you today?"}]
    if request.method == "POST":
        user_query = request.form.get("query")
        bot_response = simple_chatbot(user_query)
        messages.append({"sender": "user", "text": user_query})
        messages.append({"sender": "bot", "text": bot_response})
    return render_template_string(html_template, messages=messages)

# Run the Flask app
if __name__ == "__main__":
    app.run(port=5001)
