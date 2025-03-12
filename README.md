# DinORM - Python ORM for DinoDB

DinORM is an asynchronous, lightweight Object-Relational Mapping (ORM) library designed to interact seamlessly with the **DinoDB** database. It simplifies database operations by providing intuitive methods for CRUD functionality.

## Features
✅ Asynchronous API using `httpx` for high-performance operations.  
✅ Simplified data handling — no need to wrap data in `{ "value": {} }`.  
✅ Automatic key retrieval after successful `POST` requests.  
✅ Optional **debug mode** for detailed request/response logs.  
✅ Clean and efficient ORM structure for easy integration.  

## Installation

```bash
pip install httpx
```

## Usage

### Initialization
```python
from dinorm import DinORM
import asyncio

async def main():
    orm = DinORM("http://localhost", 8000, debug=True)
```

### POST Data
The `post()` method automatically wraps the provided data inside `{ "value": {} }`. It returns the generated key for easy reference.

```python
key = await orm.post({
    "name": "Velikiq",
    "surname": "Nepovtorimiq"
})
print("Generated Key:", key)
```

### GET Data
Retrieve data using its unique key.
```python
result = await orm.get(key)
print("Found Data:", result)
```

### DELETE Data
Delete a record by its key.
```python
await orm.delete(key)
print(f"Deleted entry with key: {key}")
```

## Example
```python
import asyncio
from dinorm import DinORM

async def main():
    orm = DinORM("http://localhost", 8000, debug=True)

    key = await orm.post({"test": 123})
    print("Generated Key:", key)

    data = await orm.get(key)
    print("Found Data:", data)

    await orm.delete(key)
    print("Entry Deleted.")

if __name__ == "__main__":
    asyncio.run(main())
```

## License
This project is licensed under the **Server Side Public License (SSPL)**. See the [LICENSE](LICENSE) file for more information.

## Contributing
Contributions are welcome! Feel free to submit pull requests or open issues for bug fixes, improvements, or feature requests.

## Contact
For inquiries or support, please open an issue on the [GitHub repository](https://github.com/yourusername/dinorm).

