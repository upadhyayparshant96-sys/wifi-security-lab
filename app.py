
from flask import Flask, request, render_template_string

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Wi-Fi Security Lab</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
    background: #101827;
    color: white;
    font-family: Arial;
    text-align: center;
    padding: 40px 15px;
}
.box {
    background: #1e293b;
    padding: 25px;
    border-radius: 15px;
    max-width: 350px;
    margin: auto;
}
input, button {
    padding: 13px;
    margin: 10px;
    width: 90%;
    border: none;
    border-radius: 8px;
}
button {
    background: #2563eb;
    color: white;
}
</style>
</head>
<body>
<div class="box">
<h2>Wi-Fi Security Lab</h2>
<p>Educational demonstration</p>

<form method="POST">
<input name="username" placeholder="Demo username" required>
<input name="password" type="password"
placeholder="Demo password" required>
<button type="submit">Test Login</button>
</form>

<p>{{ message }}</p>
<p>Demo password is never stored or displayed.</p>
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        username = request.form.get("username", "")

        print("\n--- DEMO SUBMISSION ---", flush=True)
        print("Username:", username, flush=True)
        print("Password: received (hidden)", flush=True)
        print("-----------------------", flush=True)

        message = "Demo submission received!"

    return render_template_string(PAGE, message=message)

if __name__ == "__main__":
    print("Wi-Fi Security Lab Started")
    print("Open http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000)

