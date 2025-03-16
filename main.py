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


if __name__ == "__main__":
    asyncio.run(main())
