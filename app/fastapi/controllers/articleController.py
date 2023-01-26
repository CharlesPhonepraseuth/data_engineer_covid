from fastapi import HTTPException

from common.utils import elasticsearch

# from elasticsearch import Elasticsearch
# from elasticsearch.exceptions import ConnectionError
# import os
# import time

def get_popular_section():
    """
    Get popular sections from yesterday
    """
    conn = elasticsearch.get_es_client()

    cat = ["viewed", "emailed"]

    reponse_json_final = []

    for pop_type in cat:
    # requete : afficher les sections populaires par email
        print("\nafficher les sections populaires de la veille par {}".format(pop_type))

        # On commence par chercher le nombre total d'articles

        # corps de la requete
        search_body = {
            "query": {
                "match": {
                    "popular_type": {
                        "query": pop_type # on définit la section
                    }
                }
            }
        }
        # requete python
        resp = conn.search(
            index = "popular",
            body = search_body,
        )

        # traitement de la réponse : on récupère le nombre total 
        total_doc = resp['hits']['total']['value']

        # corps de la requete pour afficher tous les docs de type "mailed" ou "viewed"
        search_body = {
            "size": total_doc,
            "query": {
                "match": {
                    "popular_type": {
                        "query": pop_type # on définit la section
                    }
                }
            }
        }

        # requete python
        resp = conn.search(
            index = "popular",
            body = search_body,
            scroll = '1m', # time value for search
        )

        # on récupère les sections
        section_list = []
        for hit in resp['hits']['hits']:
            section_list.append(hit["_source"]["article_section"])

        section_unique = list(set(section_list))

        #################################################
        # On strucure la réponse sous la forme:
        # [
        #   {
        #     "popular_by": "viewed",
        #     "details": [
        #               {
        #                "section": "Sports",
        #                 "count": 3
        #              },
        #               {
        #                "section": "Climate",
        #                 "count": 1
        #              },
        #               ]
        #   },
        #   {
        #     "popular_by": "mailed",
        #     "details": [
        #               {
        #                "section": "Sports",
        #                 "count": 
        #              }
        #               ]
        #   }
        #################################################

        # on commence par structurer les valeurs de "details" :
        details_list=[]
        for i in section_unique:
            details_value = {}
            details_value["section"] = i
            details_value["count"] = section_list.count(i)

            details_list.append(details_value)

        # on structure réponse finale :
        reponse_json={}
        reponse_json["popular_by"]=pop_type
        reponse_json["details"]=details_list
        reponse_json_final.append(reponse_json)

    return (reponse_json_final)




def get_popular_article(section):
    """
    Get popular artcile from yesterday
    Parameters
    ----------
    section : str : a popular section
    Example
    -------
    covid = get_popular_article("Sports")
    """

    conn = elasticsearch.get_es_client()

    print("\nafficher les articles populaire d'une section de la veille")

    # On commence par chercher le nombre total d'articles
    # corps de la requete
    search_body = {
        "query": {
            "match": {
                "article_section": {
                    "query": section
                }
            }
        }
    }

    # requete Python
    resp = conn.search(
        index = "popular",
        body = search_body,
        scroll = '1m', # time value for search
    )

    # traitement de la réponse : on récupère le nombre total 
    contenu = resp['hits']['hits']
    nb_articles = len(contenu)


    #################################################
    # On strucure la réponse sous la forme:
    # [
    #   {
    #     "title": "aaaaaaa",
    #     "url":  "www"
    #     },
    #   {
    #     "title": "zzzzz",
    #     "url":  "www"
    #     }
    # ]
    #################################################
    list_articles=[]
    for i in range(nb_articles):
        dico = {}
        dico['title'] = contenu[i]["_source"]["article_title"]
        dico['url'] = contenu[i]["_source"]["article_url"]

        list_articles.append(dico)

    # On supprime les articles en double (ceux qui sont populaires par "mailed" et "viewed")
    seen = set()
    liste_unique = []

    for article in list_articles:
        tuple_obj = tuple(article.items())

        if tuple_obj not in seen:
            seen.add(tuple_obj)
            liste_unique.append(article)

    print (liste_unique)

    if nb_articles == 0:
        return ("no articles, check popular section")
    else:
        return liste_unique
