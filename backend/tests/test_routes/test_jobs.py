import json 


def test_create_job(client):
    data = {
        "title" : "SDE 1 Yahoo",
        "company" : "testhoo",
        "company_url" : "https://something.com",
        "location" : "USA,NY",
        "description" : "Testing",
        "date_posted": "2022-07-20" 
    }

    response = client.post('/job/create-job', data=json.dumps(data))
    assert response.status_code == 200

def test_retrieve_job_by_id(client):
    data = {
        "title" : "SDE 1 Yahoo",
        "company" : "testhoo",
        "company_url" : "https://something.com",
        "location" : "USA,NY",
        "description" : "Testing",
        "date_posted": "2022-07-20" 
    }

    client.post('/job/create-job', data=json.dumps(data))
    response = client.get("/job/get/1")
    assert response.status_code == 200
    assert response.json()['title'] == "SDE 1 Yahoo"