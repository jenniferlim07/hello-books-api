def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }

# no data in test database (no fixture) returns a 404
def test_get_book_no_data(client, two_saved_books):
    # Act
    response = client.get("/books/5")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == None


# GET /books with valid test data (fixtures) returns a 200 
# with an array including appropriate test data
def test_get_all_books(client, two_saved_books):
    response = client.get("/books")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [ {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    },
    {
        "id": 2,
        "title": "Mountain Book",
        "description": "i luv 2 climb rocks"
    } ]


# POST /books with a JSON request body returns a 201
def test_post_book(client, two_saved_books):
    data = {
        "title": "Sky Book",
        "description": "watr 4evr"
    }
    response = client.post("/books", json=data)
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        "id": 3,
        "title": "Sky Book",
        "description": "watr 4evr"
    }
