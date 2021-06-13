from fastapi import APIRouter, HTTPException
from starlette.responses import FileResponse, StreamingResponse
import os
from io import BytesIO
from PIL import Image
import tempfile

path = "./images"
router = APIRouter()


@router.get("/{name}")
async def get_image(name: str):
    file_path = os.path.join(path, name)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404)


@router.get("/thumbnail/{name}")
async def get_thumbnail(name: str):
    file_path = os.path.join(path, name)
    if os.path.exists(file_path):
        img = Image.open("./images/" + name)
        img.convert("RGB")
        img.thumbnail((200, 200))
        buf = BytesIO()
        img.save(buf, "PNG", quality=85)
        buf.seek(0)
        # return StreamingResponse(buf, media_type="images/jpeg")
        with tempfile.NamedTemporaryFile(mode="w+b",
                                         suffix=".png",
                                         delete=False) as FOUT:
            FOUT.write(buf.read())
            return FileResponse(FOUT.name, media_type="image/png")
    else:
        raise HTTPException(status_code=404)