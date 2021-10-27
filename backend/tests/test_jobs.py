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