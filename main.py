import asyncio
from dinorm import DinORM

async def main():
    repository = DinORM("http://localhost", 8000, debug=True)

    key = await repository.post({
        "name": "Deyan",
        "surname": "Sirakov"
    })
    print("Generated Key:", key)

    if key:
        data = await repository.get(key)
        print("Found:", data)

        data = await repository.update(key, {"name": "Deyan"})
        data = await repository.get(key)
        print("Found:", data)
        
        await repository.delete(key)
        deleted_data = await repository.get(key)
        print("After Delete:", deleted_data)


async def test():
    repository = DinORM("http://localhost", port=8000, debug=False)

    resp = await repository.update("01c08731-3860-4ca9-b1d8-bf85f13c131c", { "changed": "true" })
    print("Response: ", resp)

    data = await repository.get("01c08731-3860-4ca9-b1d8-bf85f13c131c")
    print("Data: ", data)

if __name__ == "__main__":
    asyncio.run(test())
