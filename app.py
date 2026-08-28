from flask import Flask, jsonify
from routes.user_routes import user_routes


app = Flask(__name__)

# Registra as rotas de usuários
app.register_blueprint(user_routes)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "API Connect funcionando"
    }), 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)