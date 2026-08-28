from flask import Blueprint

from controllers.user_controller import (
    list_users,
    get_user,
    create_user,
    update_user,
    delete_user
)

user_routes = Blueprint("user_routes", __name__)


user_routes.route(
    "/users",
    methods=["GET"]
)(list_users)


user_routes.route(
    "/users/<int:user_id>",
    methods=["GET"]
)(get_user)


user_routes.route(
    "/users",
    methods=["POST"]
)(create_user)


user_routes.route(
    "/users/<int:user_id>",
    methods=["PUT"]
)(update_user)


user_routes.route(
    "/users/<int:user_id>",
    methods=["DELETE"]
)(delete_user)