from requests import request
from sys import argv

class Request:
    def __init__(self, method, path_api):

        #url raiz da api
        self.baseURL = "https://last-airbender-api.fly.dev/"
        self.path_api = path_api or "api/v1/characters"
        #método para a requisição
        self.method = method or "get"

    #função que retorna o caminho completo da api
    #concatena a url base com o caminho da api
    def get_full_url(self):
        path_tuple = (self.baseURL, self.path_api)
        full_url = "".join(path_tuple)
        return full_url

    #função que mostra o corpo da requisição
    def get_content(self):
        url = self.get_full_url()
        try:
            response = request(self.method, url)
            print(response.content)
        except:
            print("""
            Algo deu errado!
            verifique se a ordem dos argumentos estão corretos. 
            Exemplo do comando: python3 nome_arquivo.py my/api/v1/algo get
                  """)

#pega os argumentos passados pela linha de comando
#retorna os argumentos

def get_terminal_args():
    length_args = len(argv)
    if length_args > 3:
        print("""A quantidade de argumentos passados supera o esperado!
              Tente novamente com menos argumentos!""")
        exit(-1)
    
    elif length_args < 3:
        return argv[1], None
    
    return argv[1], argv[2]

if __name__ == "__main__":
    path_api, method = get_terminal_args()

    rq = Request(method, path_api)

    rq.get_content()
