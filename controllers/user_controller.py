from flask import request, jsonify
from data.users import users, generate_id


def list_users():
    return jsonify({
        "data": users
    }), 200


def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify({
                "data": user
            }), 200

    return jsonify({
        "error": "Usuario não encontrado"
    }), 404


def create_user():
    data = request.get_json()

    if not data or not data.get("name") or not data.get("email"):
        return jsonify({
            "error": "Nome e e-mail são obrigatórios"
        }), 400

    new_user = {
        "id": generate_id(),
        "name": data["name"],
        "email": data["email"]
    }

    users.append(new_user)

    return jsonify({
        "data": new_user
    }), 201


def update_user(user_id):
    data = request.get_json()

    if not data or not data.get("name") or not data.get("email"):
        return jsonify({
            "error": "Nome e e-mail são obrigatórios"
        }), 400

    for index, user in enumerate(users):
        if user["id"] == user_id:
            users[index]["name"] = data["name"]
            users[index]["email"] = data["email"]

            return jsonify({
                "data": users[index]
            }), 200

    return jsonify({
        "error": "Usuario não encontrado"
    }), 404


def delete_user(user_id):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            users.pop(index)
            return "", 204

    return jsonify({
        "error": "Usuario não encontrado"
    }), 404