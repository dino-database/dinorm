import httpx

class DinORM:
    """
    DinORM is a lightweight asynchronous ORM (Object-Relational Mapping) for interacting with 
    a remote data storage service via HTTP requests. It provides CRUD (Create, Read, Update, Delete) 
    functionalities with optional debug logging for improved traceability.
    """

    def __init__(self, url: str, port: int, debug: bool = False):
        """
        Initializes the DinORM instance.

        Args:
            url (str): The base URL of the remote data storage service.
            port (int): The port on which the service is running.
            debug (bool, optional): Enables debug logging if True. Defaults to False.
        """
        self.base_url = f"{url}:{port}"
        self.debug = debug

    def _log(self, message: str):
        """
        Logs debug messages if debugging is enabled.

        Args:
            message (str): The message to log.
        """
        if self.debug:
            print(message)

    async def post(self, data: dict) -> str | None:
        """
        Sends a POST request to add new data to the remote storage.

        Args:
            data (dict): The data to be stored.

        Returns:
            str | None: The key of the stored data if successful; otherwise, None.
        """
        payload = {"value": data}
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(f"{self.base_url}/data/add", json=payload)
                response.raise_for_status()
                response_data = response.json()

                self._log(f"Post Response code: {response.status_code}")
                self._log(f"Post Response: {response_data}")

                return response_data.get("key")
            except httpx.HTTPStatusError as e:
                self._log(f"HTTP error: {e}")
            except httpx.RequestError as e:
                self._log(f"Request error: {e}")
            return None

    async def update(self, key: str, data: dict) -> bool:
        """
        Sends a PATCH request to update data associated with a given key.

        Args:
            key (str): The key identifying the data to update.
            data (dict): The new data to store.

        Returns:
            bool: True if the update was successful; otherwise, False.
        """
        payload = {"value": data}
        async with httpx.AsyncClient() as client:
            try:
                response = await client.patch(f"{self.base_url}/data/update/{key}", json=payload)
                response.raise_for_status()
                response_data = response.json()

                self._log(f"Update Response code: {response.status_code}")
                self._log(f"Update Response: {response_data}")

                return True
            except httpx.HTTPStatusError as e:
                self._log(f"HTTP error: {e}")
            except httpx.RequestError as e:
                self._log(f"Request error: {e}")
            return False

    async def get(self, key: str) -> dict | None:
        """
        Sends a GET request to retrieve data associated with a given key.

        Args:
            key (str): The key identifying the data to retrieve.

        Returns:
            dict | None: The requested data if found; otherwise, None.
        """
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.base_url}/data/get/{key}")
                return response.json().get("value")
            except httpx.HTTPStatusError as e:
                self._log(f"HTTP error: {e}")
            except httpx.RequestError as e:
                self._log(f"Request error: {e}")
            return None

    async def delete(self, key: str) -> bool:
        """
        Sends a DELETE request to remove data associated with a given key.

        Args:
            key (str): The key identifying the data to delete.

        Returns:
            bool: True if the deletion was successful; otherwise, False.
        """
        async with httpx.AsyncClient() as client:
            try:
                response = await client.delete(f"{self.base_url}/data/delete/{key}")
                self._log(f"Delete Response code: {response.status_code}")
                self._log(f"Delete Response: {response.text}")
                return True
            except httpx.HTTPStatusError as e:
                self._log(f"HTTP error: {e}")
            except httpx.RequestError as e:
                self._log(f"Request error: {e}")
            return False