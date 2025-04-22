import json
import asyncio
from APIRequest import Request
from Translator import translate_list

def extract_keys(dictionary:dict):
    keys_list = dictionary.keys()
    return keys_list



if __name__ == '__main__':
    baseURL = "https://last-airbender-api.fly.dev/"
    api_path = "api/v1/characters"
    method = "get"
    

    request = Request(method, baseURL,api_path)
    content = request.get_content()
    
    #get keys of the dictionary
    keys_list = extract_keys(content[1])
    translated_keys = asyncio.run(translate_list(keys_list, 'pt'))
    print(translated_keys)
    #print(json.dumps(content, indent=4))


