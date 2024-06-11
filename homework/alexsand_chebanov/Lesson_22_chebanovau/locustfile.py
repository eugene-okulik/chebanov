from locust import task, HttpUser


class ApiRestful(HttpUser):
    created_users = []

    @task
    def get_all_objects(self):
        self.client.get(
            '/objects'
        )

    @task
    def post_request(self):
        body = {
            "name": "Apple MacBook Pro 77",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
        response = self.client.post("/objects", json=body)
        user_id = response.json()["id"]
        self.created_users.append(user_id)
        print(f"Created user with ID: {user_id}")

    @task
    def put_request(self):
        if self.created_users:
            user_id = self.created_users.pop()

            data = {
                "name": "Apple MacBook Pro 16",
                "data": {
                    "year": 2019,
                    "price": 2049.99,
                    "CPU model": "Intel Core i9",
                    "Hard disk size": "1 TB",
                    "color": "silver"
                }
            }
            self.client.put(f"/objects/{user_id}", json=data)
            print(f"Updated user with ID: {user_id}")

    @task
    def delete_request(self):
        response = self.client.delete("/objects")
        user_id = response.json()["id"]
        self.created_users.append(user_id)
        print(f"Delete user with ID: {user_id}")
