from flask import Flask

from mtj.flask.pdns.blueprint import mtj_pdns


app = Flask(__name__)
app.register_blueprint(mtj_pdns, url_prefix='/pdns')
