from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h3>Kalkulator Python Sederhana</h3>
    <form action="/calculate" method="GET">
        <input type="text" name="math" placeholder="Contoh: 5 * 5">
        <input type="submit" value="Hitung">
    </form>
    """

@app.route('/calculate')
def calculate():
    user_input = request.args.get('math', '')
    
    try:
        result = eval(user_input)
        
        return f"Hasil dari {user_input} adalah: <b>{result}</b>"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, port=5000)