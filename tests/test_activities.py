def test_get_activities_returns_activity_map(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_get_activities_includes_participants_list(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    chess = data["Chess Club"]
    assert isinstance(chess["participants"], list)
    assert "michael@mergington.edu" in chess["participants"]
