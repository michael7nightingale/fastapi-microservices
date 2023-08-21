from fastapi import Request

from core import GateWay


app = GateWay()


@app.route("get", "/{user_id}", "12", None, None)
async def home(request: Request, user_id, chat):
    pass
