from sqlalchemy import text
from sqlalchemy.orm.session import Session


def fetch_one(query: str, queryargs: dict, *, db: Session):
    textual_query = text(query)
    result = db.execute(textual_query, queryargs).fetchone()
    print(type(result))
    return dict(result)


def fetchall(query: str, queryargs: dict, db: Session):
    textual_query = text(query)
    resultproxy = db.execute(textual_query, queryargs)
    # d, a = {}, []
    # for rowproxy in resultproxy:
    #     # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
    #     for column, value in rowproxy.items():
    #         # build up the dictionary
    #         d = {**d, **{column: value}}
    #     a.append(d)
    # return a
    return [dict(row) for row in resultproxy]


import inspect
from typing import Type
from fastapi import Form
from pydantic.errors import StrRegexError
from pydantic import BaseModel


def as_form(cls: Type[BaseModel]):
    """
    Adds an as_form class method to decorated models. The as_form class method
    can be used with FastAPI endpoints
    """
    new_params = [
        inspect.Parameter(
            field.alias,
            inspect.Parameter.POSITIONAL_ONLY,
            default=(Form(field.default) if not field.required else Form(...)),
        ) for field in cls.__fields__.values()
    ]

    async def _as_form(**data):
        return cls(**data)

    sig = inspect.signature(_as_form)
    sig = sig.replace(parameters=new_params)
    _as_form.__signature__ = sig
    setattr(cls, "as_form", _as_form)
    return cls


from PIL import Image
from io import BytesIO
import uuid


def saveimg(image, quality=85, *, name=None, url=True):
    if name is None:
        name = str(uuid.uuid4())
    name += ".png"
    img = Image.open(image.file)
    buf = BytesIO()
    img.save(buf, "PNG", quality=quality)
    buf.seek(0)
    with open("./images/" + str(name), 'wb') as f:
        # f.write(content)
        try:
            f.write(buf.read())
        except Exception as e:
            print(e)
    if url:
        return "/img/" + name
    else:
        return name
