from fastapi import status,HTTPException
from unittest.mock import patch
from jose import JWTError
from app.main import app
from app.api.routes.api_key import get_current_user

# create appi

def test_create_APIKey(client):
    payload={
    "id": 1,
    "key_name": "test_key",
    "is_active": True,
    "request_counter": 0
    }

    app.dependency_overrides[get_current_user] = lambda: {"email": "test@gmail.com"}

    with patch("app.api.routes.api_key.create_api") as mock_create:
        
        mock_create.return_value = None

        response = client.post("/Api_Mangement/create", json=payload)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"msg": "api created"}



# view api dat
def test_view_all_APIKey(client):

    app.dependency_overrides[get_current_user] = lambda: {"email": "test@gmail.com"}

    with patch("app.api.routes.api_key.get_all_api") as mock_get_api:
        
        mock_get_api.return_value =[{"_id": 1,"key_name": "testAPIKey","is_active": True,"request_counter": 0,"last_call_time": "2026-04-20T10:45:30.123456"}]

        response = client.get("/Api_Mangement/view")

        assert response.status_code == status.HTTP_200_OK
        assert response.json() ==[{"_id": 1,"key_name": "testAPIKey","is_active": True,"request_counter": 0,"last_call_time": "2026-04-20T10:45:30.123456"}]

def test_view_one_APIKey(client):
    app.dependency_overrides[get_current_user] = lambda: {"email": "test@gmail.com"}

    with patch("app.api.routes.api_key.get_single_api") as mock_get_api:
        
        mock_get_api.return_value =[{"_id": 1,"key_name": "testAPIKey","is_active": True,"request_counter": 0,"last_call_time": "2026-04-20T10:45:30.123456"}]

        response = client.get("/Api_Mangement/view/1")

        assert response.status_code == status.HTTP_200_OK
        assert response.json() ==[{"_id": 1,"key_name": "testAPIKey","is_active": True,"request_counter": 0,"last_call_time": "2026-04-20T10:45:30.123456"}]

# delete api

def test_delete_APIKey(client):
    app.dependency_overrides[get_current_user] = lambda: {"email": "test@gmail.com"}

    with patch("app.api.routes.api_key.delete_api") as mock_delete_api:
        
        mock_delete_api.return_value = {
            "msg": "api deleted successfully"
        }

        response = client.delete("/Api_Mangement/delete/1")

        assert response.status_code == status.HTTP_200_OK
        assert response.json() =={
            "msg": "api deleted successfully"
        }

def test_delete_APIKey_NotFound(client):
    app.dependency_overrides[get_current_user] = lambda: {"email": "test@gmail.com"}

    with patch("app.api.routes.api_key.delete_api") as mock_delete_api:
        
        mock_delete_api.side_effect = HTTPException(
            status_code=404,
            detail="api Not found"
        )

        response = client.delete("/Api_Mangement/delete/1")

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() =={
            "detail":"api Not found"
        }


# update api

def test_update_APIKey_activate(client):

    app.dependency_overrides[get_current_user] = lambda: {"email": "test@gmail.com"}

    with patch("app.api.routes.api_key.update_api") as mock_update_api:
        
        mock_update_api.return_value={
            "msg": "api deleted successfully"
        }

        response = client.put("/Api_Mangement/update/1",params={"activate": True})

        assert response.status_code == status.HTTP_200_OK
        assert response.json() =={
            "msg": "api deleted successfully"
        }


def test_update_APIKey_deactivate(client):
    app.dependency_overrides[get_current_user] = lambda: {"email": "test@gmail.com"}

    with patch("app.api.routes.api_key.update_api") as mock_update_api:
        
        mock_update_api.return_value={
            "msg": "api deactivated"
        }

        response = client.put("/Api_Mangement/update/1",params={"activate": False})

        assert response.status_code == status.HTTP_200_OK
        assert response.json() =={
            "msg": "api deactivated"
        }

def test_update_APIKey_NotFound(client):
    app.dependency_overrides[get_current_user] = lambda: {"email": "test@gmail.com"}

    with patch("app.api.routes.api_key.update_api") as mock_update_api:
        
        mock_update_api.side_effect = HTTPException(
            status_code=404,
            detail="api Not found"
        )

        response = client.put("/Api_Mangement/update/1",params={"activate": False})

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() =={
            "detail":"api Not found"
        }