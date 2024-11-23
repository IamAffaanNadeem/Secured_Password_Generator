from flask import Flask, render_template, request, jsonify
import secrets
import string

app = Flask(__name__)

# Function to generate a secure password
def generate_password(length=16, include_special=True):
    if length < 12:
        return {"error": "Password length should be at least 12 characters."}

    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation if include_special else ""

    # Ensure at least one of each type is included
    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
    ]
    if include_special:
        password.append(secrets.choice(special))

    # Fill the rest of the password length with random choices
    all_characters = uppercase + lowercase + digits + special
    password += [secrets.choice(all_characters) for _ in range(length - len(password))]

    # Shuffle and return the password
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-password', methods=['POST'])
def generate():
    data = request.json
    length = data.get('length', 16)
    include_special = data.get('include_special', True)
    password = generate_password(length, include_special)
    if isinstance(password, dict):  # If there's an error
        return jsonify(password), 400
    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(debug=True)
