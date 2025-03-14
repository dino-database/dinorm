import httpx
import asyncio

class DinORM:
    def __init__(self, url: str, port: int, debug: bool = False):
        self.base_url = f"{url}:{port}"
        self.debug = debug

    def _log(self, message: str):
        if self.debug:
            print(message)

    async def post(self, data: dict) -> str | None:
        """
        Returns the key
        """
        payload = {"value": data}  # Auto-wrap the data
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
        
    async def update(self, key, data: dict) -> str | None:
        payload = {"value": data}  # Auto-wrap the data
        async with httpx.AsyncClient() as client:
            try:
                response = await client.patch(f"{self.base_url}/data/update/{key}", json=payload)
                response.raise_for_status()
                response_data = response.json()

                self._log(f"Update Response code: {response.status_code}")
                self._log(f"Update Response: {response_data}")

                return response_data.get("key")
            except httpx.HTTPStatusError as e:
                self._log(f"HTTP error: {e}")
            except httpx.RequestError as e:
                self._log(f"Request error: {e}")
            return None
        

    async def get(self, key: str):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.base_url}/data/get/{key}")
                return response.json()["value"]
            except httpx.HTTPStatusError as e:
                self._log(f"HTTP error: {e}")
            except httpx.RequestError as e:
                self._log(f"Request error: {e}")
            return None

    async def delete(self, key: str):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.delete(f"{self.base_url}/data/delete/{key}")
                self._log(f"Delete Response code: {response.status_code}")
                self._log(f"Delete Response: {response.text}")
            except httpx.HTTPStatusError as e:
                self._log(f"HTTP error: {e}")
            except httpx.RequestError as e:
                self._log(f"Request error: {e}")
