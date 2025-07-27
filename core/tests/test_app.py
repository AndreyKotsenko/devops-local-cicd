from core.app import app

def test_home():
    with app.test_client() as client:
        res = client.get("/")
        assert res.status_code == 200
        assert res.get_json()["message"] == "Hello, DevOps World!"

def test_health():
    with app.test_client() as client:
        res = client.get("/health")
        assert res.status_code == 200
        assert res.get_json()["status"] == "ok"
