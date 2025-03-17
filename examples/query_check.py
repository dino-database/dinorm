from .dinorm.dinorm import DinORM

def run():
    orm = DinORM("localhost", port=8000, debug=True)
    print("Here!")

if __name__ == "__main__":
    run()