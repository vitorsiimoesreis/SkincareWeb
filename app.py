from flask import Flask, render_template
from usuario_dao import UsuarioDAO

app = Flask(__name__)
dao = UsuarioDAO()

@app.route('/')
def index():
    conn = dao.listar_usuarios()
    return render_template('index.html', usuarios=conn)

if __name__ == '__main__':
    app.run(debug=True)