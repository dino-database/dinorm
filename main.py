import asyncio
from dinorm import DinORM

async def main():
    orm = DinORM("http://localhost", 8000, debug=True)

    key = await orm.post({
        "name": "Velikiq",
        "surname": "Nepovtorimiq"
    })
    print("Generated Key:", key)

    if key:
        data = await orm.get(key)
        print("Found:", data)

        data = await orm.update(key, {"name": "Deyan"})
        data = await orm.get(key)
        print("Found:", data)
        
        await orm.delete(key)
        deleted_data = await orm.get(key)
        print("After Delete:", deleted_data)

if __name__ == "__main__":
    asyncio.run(main())
