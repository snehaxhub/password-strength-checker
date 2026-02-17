from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def check():
    strength = ""
    rules = {}

    if request.method == 'POST':
        password = request.form['password']
        score = 0
        rules = {
    "length": len(password) >= 8,
    "upper": any(c.isupper() for c in password),
    "lower": any(c.islower() for c in password),
    "digit": any(c.isdigit() for c in password),
    "special": any(not c.isalnum() for c in password)
}


        if len(password) >= 8:
            score += 1
        if any(c.isupper() for c in password):
            score += 1
        if any(c.islower() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(not c.isalnum() for c in password):
            score += 1

        if score <= 2:
            strength = "Weak"
        elif score <= 4:
            strength = "Medium"
        else:
            strength = "Strong"

    return render_template('index.html', result=strength, rules=rules)

app.run(debug=True)
