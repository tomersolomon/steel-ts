import requests

class TodoClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def create_todo(self, todo):
        response = requests.post(f"{self.base_url}/todos/", json=todo)
        response.raise_for_status()
        return response.json()

    def get_todo(self, todo_id):
        response = requests.get(f"{self.base_url}/todos/{todo_id}")
        response.raise_for_status()
        return response.json()

    def update_todo(self, todo_id, todo):
        response = requests.put(f"{self.base_url}/todos/{todo_id}", json=todo)
        response.raise_for_status()
        return response.json()

    def delete_todo(self, todo_id):
        response = requests.delete(f"{self.base_url}/todos/{todo_id}")
        response.raise_for_status()
        return response.json()


# Test creating a to-do
if __name__ == "__main__":
    # Initialize the client with the base URL of your API
    client = TodoClient(base_url="http://127.0.0.1:8000")

    # Create a new to-do (make sure 'name' is used instead of 'title')
    new_todo = {
        "id": 1,
        "name": "Buy groceries",  # 'name' instead of 'title'
        "description": "Get milk, eggs, and bread."
    }

    # Test creating the to-do
    try:
        created_todo = client.create_todo(new_todo)
        print("Created Todo:", created_todo)
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
