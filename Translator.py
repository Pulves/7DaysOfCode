from googletrans import Translator

#traduz uma lista de palavras
#input: words:lista de palavras,
#language_dest: linguagem para a qual deve ser traduzido
#output: lista de palavras traduzidas
async def translate_list(words:list[str], language_dest:str):
   async  with Translator() as trans:
        try:
            translated_words = await trans.translate(words, dest=language_dest)
        except Exception as error:
            return f'''
            Erro ao traduzir as palavras!
            [#] Detalhes do erro: {error}
            '''
        if isinstance(translated_words, list):
            return [translated.text for translated in translated_words]
        else:
            return translated_words.text

