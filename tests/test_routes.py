
def test_get_all_books_with_no_records(client):
    response = client.get("/books")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_book_by_id(client, add_two_books):
    response = client.get("/books/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Ocean Book",
        "description": "water 4ever"
    }

def test_create_one_book(client):
    response = client.post("/books", json={"title": "New Book",
        "description": "The Best!"})
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Book New Book created"