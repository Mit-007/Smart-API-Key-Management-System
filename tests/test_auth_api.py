from fastapi import status
from unittest.mock import patch
from jose import JWTError

def test_register_user(client):
    payload = {
        "email": "test1@gmail.com",
        "password": "test1"
    }

    response = client.post("/auth/register",json = payload)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"msg": "User created"}

def test_login_suceess(client):
    payload = {
        "email": "test1@gmail.com",
        "password": "test1"
    }

    with patch("app.api.routes.auth.authenticate_user") as mock_auth ,\
         patch("app.api.routes.auth.create_access_token") as mock_access,\
         patch("app.api.routes.auth.create_refresh_token") as mock_refresh :
        
        mock_auth.return_value = {"email":"test1@gamil.com"}
        mock_access.return_value = "fake_access_token"
        mock_refresh.return_value = "fake_refresh_token"

        response = client.post("/auth/login",json=payload)
        
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            "access_token": "fake_access_token",
            "refresh_token": "fake_refresh_token",
            "token_type": "bearer"
        }  


def test_login_invlaid_credentials(client):
    payload = {
        "email":"wrongtest@gmail.com",
        "password":"wrongpassword"
    }

    with patch("app.api.routes.auth.authenticate_user") as mock_auth:

        mock_auth.return_value = None

        response = client.post("/auth/login",json=payload)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

        assert response.json() == {
            "detail":"Invalid credentials"
        }


def test_refresh_token_suceess(client):
    with patch("app.api.routes.auth.jwt.decode") as mock_decode,\
         patch("app.api.routes.auth.create_access_token") as mock_aceess:
        
        mock_decode.return_value={
            "sub":"test@gmail.com",
            "type":"refresh"
        }

        mock_aceess.return_value = "new_access_token"

        response = client.post("/auth/refresh",json="valid_refresh_token")

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            "access_token":"new_access_token"
        }

def test_refresh_token_invalidType(client):
    with patch("app.api.routes.auth.jwt.decode") as mock_decode :

        mock_decode.return_value = {
            "sub":"test@gmail.com",
            "type":"access"
        }

        response = client.post("/auth/refresh",json="wrong_type_token")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

        assert response.json() == {
            "detail":"invalid token type"
        }

def test_refresh_token_invalid(client):
    with patch("app.api.routes.auth.jwt.decode") as mock_decode :

        mock_decode.side_effect = JWTError()

        response = client.post("/auth/refresh",json="invalid_token")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

        assert response.json() == {
            "detail":"Invalid and expired refresh token"
        }