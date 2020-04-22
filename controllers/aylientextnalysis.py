import utils.utils as utils
from aylienapiclient import textapi

# Agotado yhomii.cloud
# APP_ID="236f2621"
# API_KEY="7a388349f12393dfe3e11be438ac6ae9"

# juancsr
APP_ID="fc10cf54"
API_KEY="468a71e8c39d17e16241dafb68a81c2f"

"""
Construye un diccionario con el resultado completo del análisis de una página que lleva a una url, compuesto por: 
* clasificación
* sentimientos
* entidades
* Conceptos
* Resumen

:param url: url de la página a analizar
:return: un diccionario con toda la información del análisis
"""
def performsFullAnalysis(url):
    result = {}
    try:
        result['classification'] = performClassificationAnalysis(url)
        result['text'] = result['classification']['text']
        result['sentiment'] = performSentimentAnalysis(url)
        result['entity'] = performElsaAnalysis(url)
        result['concepts'] = performConceptAnayalisis(url)
        result['summary'] = performSummayAnalysis(url)
        for key in result.keys():
            if key is not 'text':
                print(key)
                del result[key]['text']
    except:
        utils.logger("error perfom the full anayalusis", "performsFullAnalysis")
    return result

""" 
Utilizando el SDK de aylien, realiza el análisis de sentimientos

:param url: url de la página a análisar
:return: un diccionario con la información del resultado del análisis
"""
def performClassificationAnalysis(url):
    client = textapi.Client(APP_ID, API_KEY)
    classifications = client.Classify({'url': url})
    return classifications

""" 
Utilizando el SDK de aylien, realiza el análisis de sentimientos

:param url: url de la página a análisar
:return: un diccionario con la información del resultado del análisis
"""
def performSentimentAnalysis(url):
    client = textapi.Client(APP_ID, API_KEY)
    sentiment = client.Sentiment({'url': url})
    return sentiment


""" 
Utilizando el SDK de aylien, realiza el análisis de entidades (por ejemplo personas, organzaciones, productos)

:param url: url de la página a análisar
:return: un diccionario con la información del resultado del análisis
"""
def performElsaAnalysis(url):
    client = textapi.Client(APP_ID, API_KEY)
    elsa = client.Elsa({'url': url})
    return elsa

""" 
Utilizando el SDK de aylien, realiza el análisis de conceptos, es decir, información de las palabras utilizadas en el web site

:param url: url de la página a análisar
:return: un diccionario con la información del resultado del análisis
"""
def performConceptAnayalisis(url):
    client = textapi.Client(APP_ID, API_KEY)
    concepts = client.Concepts({'url': url})
    return concepts

""" 
Utilizando el SDK de aylien, realiza el resumen de árticulo en el web site

:param url: url de la página a análisar
:return: un diccionario con la información del resultado del análisis
"""
def performSummayAnalysis(url, setences_number=3):
    client = textapi.Client(APP_ID, API_KEY)
    summary = client.Summarize({'url': url, 'sentences_number': setences_number})
    return summary
