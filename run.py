import sys
import uvicorn
from dotenv import load_dotenv
import os
PATH = os.getcwd()
if __name__=="__main__":
    if sys.argv[1]=="dev":
        env = os.path.join(PATH, "api\\dev.env")
    else:
        env = os.path.join(PATH, "api\\.env")
    load_dotenv(env, verbose=True)
    print(os.environ.get("DBHOST"))
    uvicorn.run("api.main:app", host="127.0.0.1", port=5000, log_level="info")