from requests import request

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
        url = self._concatene_url()
        try:
            response = request(self.method, url)
           
        except Exception as error:
            return f'''
            Erro ao fazer a requisição para API!
            [#]detalhe do erro: {error}
            '''
        return response.json()



