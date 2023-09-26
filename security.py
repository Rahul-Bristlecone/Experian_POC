import hmac
from models.user import UserModel


def authenticate(username, password):
    """
    this function gets called when we call the "/auth" end-point, this end-point is hit when the user send us the
    username and password. We are not implementing the end-point because flask-Jwt automatically takes care of it.
    So, we are not implementing the JWT but still we will be checking if they are correct or not.
    we will return the user if the authentication was successful.
    :return UserModel object (by Jsonifying it)
    """

    user = UserModel.find_by_username(username)
    if user and hmac.compare_digest(user.password, password):
        return user


def identity(payload):
    """
    If the user is already logged-in (authenticated), then we will receive the token in header from the user
    in header of the request. Flask-jwt will decode it and give us the payload in the form of dictionary.
    """
    user_id = payload["id"]
    return UserModel.find_by_userid(user_id)