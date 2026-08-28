users = [
    {
        "id": 1,
        "name": "Carlos Silva",
        "email": "carlos@email.com"
    },
    {
        "id": 2,
        "name": "Ana Souza",
        "email": "ana@email.com"
    }
]

next_id = 3


def generate_id():
    global next_id

    new_id = next_id
    next_id += 1

    return new_id