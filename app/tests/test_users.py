# from fastapi.testclient import TestClient
# from app.main import app
# import uuid

# client = TestClient(app)

# def test_create_user():
#     # Generate a unique email for the test
#     unique_email = f"test_{uuid.uuid4()}@example.com"

#     response = client.post(
#         "/users/",
#         json={"email": unique_email, "password": "securepassword"}
#     )

#     assert response.status_code == 200
#     assert response.json()["email"] == unique_email
