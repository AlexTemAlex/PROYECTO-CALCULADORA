from flask import Flask, render_template, request

app = Flask(__name__)

def sumar(a, b):
    return a + b

@app.route('/', methods=['GET', 'POST'])
def home():
    res = None
    if request.method == 'POST':
        try:
            n1 = float(request.form['val1'])
            n2 = float(request.form['val2'])
            res = sumar(n1, n2)
        except:
            res = "Error"
    return render_template('index.html', resultado=res)

if __name__ == '__main__':
    # Host 0.0.0.0 es obligatorio para Docker
    app.run(host='0.0.0.0', port=5000)
