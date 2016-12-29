# Sanic
from sanic import Sanic
from sanic.response import json


app = Sanic()


@app.route("/")
async def test(request):
    return json({"hello": "world"})
