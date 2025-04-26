#função lambda que retorna um dicionário da lista de chaves e valores 
create_dict = lambda keys, values : dict(zip(keys, list(values)))

#extrai as chaves do dicionário
#a entrada é um dicionário
#retorna uma lista de chaves
def extract_keys(dictionary:dict):
    keys_list = dictionary.keys()
    return [key for key in keys_list]


#muda as chaves de dicionário
#cria um dicionário novo com as chaves novas e o conteudo das chaves antigas
#as entradas são uma lista de chaves novas, as chaves antigas
#e a lista de dicionários

def change_dict_keys(new_keys:list, old_keys:list, list_content:list) -> list:
    
    new_dict_list = []
    #intera o dicionário
    for dictionary in list_content:
        #verifica o tamanho
        #se ele for menor vai ser preciso encontrar as chaves existentes
        if len(dictionary) < 6:
            index_list = index_keys(old_keys, dictionary)#pega a posição das chaves na lista
            keys_list = element_by_index(new_keys, index_list)#pega os elementos da lista baseado nas chaves
            
            new_dict_list.append(
                    create_dict(keys_list, dictionary.values())
                    )
            
        else:
            new_dict_list.append(
                    create_dict(new_keys, dictionary.values())
                    )
    

    return new_dict_list


#pega o elemento da lista pelo index
#entradas: ums lista contendo os elementos
#uma lista contendo os indices(posições) dos elementos
#saida: uma lista de elementos baseada nos indices
def element_by_index(elements:list, indexes:list) -> list:
    
    return [
            elements[index]
            for index in indexes
            ]

#pega os indices(posições) das chaves
#entradas: uma lista de chaves e um dicionário
#saida: uma lista de indices(posições)
def index_keys(keys:list, dictionary:dict) -> list:
    list_index = []
    for key in dictionary.keys():
        if key in keys:
            list_index.append(keys.index(key))
    return list_index



"""if __name__ == '__main__':
    baseURL = "https://last-airbender-api.fly.dev/"
    api_path = "api/v1/characters"
    method = "get"
    

    request = Request(method, baseURL,api_path)
    content = request.get_content()
    
    #get keys of the dictionary
    keys_list = extract_keys(content[1])
    
    translated_keys = asyncio.run(translate_list(keys_list, 'pt'))
    
    
    
    new_content = change_dict_keys(translated_keys, keys_list, content)
    print(json.dumps(new_content, indent=4))

"""