''' Determine if keywords are in site.'''

import requests

def has_keywords(spark, faculty_pages, keywords):
    '''Sites has keywords?'''
    profs = spark.sparkContext.parallelize(faculty_pages)
    return (profs
            .filter(lambda x: check_site(x, keywords))
            .collect())

def check_site(path, keywords):
    ''' Does site contain keywords?'''
    keywords = [e+' ' for e in keywords]
    content = requests.get(path, timeout=10).text
    rez = False
    for e in keywords:
        if e in content:
            rez = True
            break
    return rez
