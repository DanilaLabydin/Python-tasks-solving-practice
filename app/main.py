from fastapi import FastAPI


app = FastAPI()


COLUMN_NAME = "name"
COLUMN_ID = "id"
FAKE_DB = [
    {"id": 1, "name": "Vladimir"},
    {"id": 2, "name": "Polina"},
    {"id": 3, "name": "Aleksander"}
]


def find_friend_name(friend_id, db_name):
    for row in db_name:
        if row.get(COLUMN_ID) == friend_id:
            return row.get(COLUMN_NAME)

    return None


@app.get("/friends/{friend_id}")
async def get_friend_name(friend_id: int):
    friend_name = find_friend_name(friend_id, FAKE_DB)
    if friend_name is None:
        return {"error": f"No such friend with id {friend_id}"}

    return {"friend_name": friend_name}


@app.get("/")
async def root():
    return {"message": "Hello world!"}



