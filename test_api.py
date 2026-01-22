import requests

BASE_URL = "http://127.0.0.1:8000"

# Test /match endpoint
match_data = {
    "resume_text": "I know Python, FastAPI, SQL",
    "jd_text": "Looking for Python, FastAPI skills"
}
match_resp = requests.post(f"{BASE_URL}/match", json=match_data)
print("MATCH RESPONSE:", match_resp.json())

# Test /gap endpoint
gap_data = {
    "resume_text": "I know Python, FastAPI",
    "jd_text": "Looking for Python, FastAPI, SQL"
}
gap_resp = requests.post(f"{BASE_URL}/gap", json=gap_data)
print("GAP RESPONSE:", gap_resp.json())
