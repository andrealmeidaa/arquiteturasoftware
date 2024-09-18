from controles.tarefa_controler import api
import uvicorn

if __name__ == "__main__":
    uvicorn.run(api, host="127.0.0.1",port=8000)