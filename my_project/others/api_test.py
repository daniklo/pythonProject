import pytest
import requests




response = requests.get("http://localhost:3000/posts", params={"id" : id})
json_response = response.json()
print(json_response)

data_test = [
    (0,1,"updated title"),
    (1,2,"json-2"),
    (2,3,"the best titlee"),
    (3,4,"aa")
]

@pytest.mark.parametrize("order,id,title", data_test)
def test_api(order ,id,title) :
    response = requests.get(f"http://localhost:3000/posts", params={"id": {id}})
    json_response = response.json()
    print(json_response)
    assert  json_response[0]["id"] == id
    assert json_response[0]["title"] == title


