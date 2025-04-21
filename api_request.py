from requests import request

#url raiz da api
#baseURL = "https://last-airbender-api.fly.dev/"
#path_api = "api/v1/characters"
#caminho completo para pegar os dados da api
#concatena a url raiz(baseURL) com o caminho da api (path_api)
#full_url = "".join((baseURL, path_api))
#método para a requisição
#method = "get"

#função que mostra o corpo da requisição
#def get_content(method: str, url: str):
 #   response = request(method, url)
  #  print(response.content)

#chamada da função
#get_content(method=method, url=full_url)


class Request:
   def  __init__(self, method: str, baseURL:str, path_api:str):
       self.method = method
       self.baseURL = baseURL
       self.path_api = path_api

    def _concatene_url(self):
       full_path_tuple = (self.baseURL, self.path_api)
       full_path = "".join(full_path_tuple)
       return full_path

   def get_content(self):
       url = _concatene_url()
       try:
           response = request(self.method, url)
           
       except Exception as error:
           return f'''
           Erro ao fazer a requisição para API!
           [#]detalhe do erro: {error}
           '''
       return response.content



