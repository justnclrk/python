from flask import Flask, render_template
app = Flask(__name__)
@app.route('/hello')
def justin():
    return render_template('index.html')
app.run(debug=True)