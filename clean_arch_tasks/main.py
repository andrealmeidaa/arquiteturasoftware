from controles.tarefa_controler import api
import uvicorn

if __name__ == "__main__":
    uvicorn.run(api, host="127.0.0.1",port=8000)

# Swagger em https:<codespace_host>/docs. Se local: localhost:8000/host
#mais informações: https://fastapi.tiangolo.com/deployment/manually/#run-the-server-program