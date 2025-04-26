import asyncio
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from APIRequest import Request
from Translator import translate_list
from KeysModifier import change_dict_keys, extract_keys

# Create your views here.
def index(request):

    context = {
        'title': "third day"
    }
    return render(request, 'index.html', context)

def get_characters(request):

    baseURL = "https://last-airbender-api.fly.dev/"
    api_path = "api/v1/characters"
    method = "get"

    if request.method == 'GET':

        rq = Request(method=method, baseURL=baseURL, path_api=api_path)
        characters = rq.get_content()
        keys = extract_keys(characters[1])
        translated_keys = asyncio.run(translate_list(keys, 'pt'))
        characters_translated = change_dict_keys(translated_keys, keys, characters)

        response = interate_characters(characters_translated)
        context = {
            'title': 'Personagesn Traduzidos',
            'characters': response
        }
        return render(request, 'characters.html', context)
    
    else:
        return HttpResponseBadRequest("Método não suportado!")



def interate_characters(characters):

    filtered_characters = []

    for caracter in characters:
        if 'afiliação' in caracter.keys():
            filtered_characters.append(
                {
                    'nome': caracter['nome'],
                    'afiliacao': caracter['afiliação'],
                    'aliados': ' '.join(caracter['aliados']),
                    'inimigos': ' '.join(caracter['inimigos'])
                }
            )
        else:
            filtered_characters.append(
                {
                    'nome': caracter['nome'],
                    'afiliacao': '',
                    'aliados': ' '.join(caracter['aliados']),
                    'inimigos': ' '.join(caracter['inimigos'])
                }
            )

    return filtered_characters