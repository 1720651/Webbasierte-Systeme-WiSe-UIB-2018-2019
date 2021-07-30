from flask import *
# Flask-App definieren
# Pfad /
app = Flask(__name__)
@app.route('/')
def start():
    #auf Index umleiten
    return redirect(url_for('index'))
# Pfad /index
@app.route('/index')
def index():
    # index.html anzeigen
    return render_template('index.html')
# Pfad /answer
@app.route('/answer')
def answer():
    # answer.html anzeigen                    Model-Parameter für die View (Template)
    return render_template('answer.html', vorname=request.args['vorname'],nachname=request.args['nachname'])