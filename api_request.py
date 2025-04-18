from requests import request

#url raiz da api
baseURL = "https://last-airbender-api.fly.dev/"
path_api = "api/v1/characters"
#caminho completo para pegar os dados da api
#concatena a url raiz(baseURL) com o caminho da api (path_api)
full_url = "".join((baseURL, path_api))
#método para a requisição
method = "get"

#função que mostra o corpo da requisição
def get_content(method: str, url: str):
    response = request(method, url)
    print(response.content)

#chamada da função
get_content(method=method, url=full_url)

