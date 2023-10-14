'''Get faculty pages'''

import requests

def get_cs_faculty():
    ''' Get all CS faculty pages'''
    return {'cs': {}}

def get_mfe_faculty():
    ''' Get all MFE faculty pages'''
    return {'mfe':[]}

def get_uta_cs_faculty():
    '''Get UT Austin CS faculty webpages'''
    base_path = get_uta_cs_base_path()
    print(f'Parsing: {base_path}')
    content = requests.get(base_path, timeout=10).content
    sources = '>'.join([e for e in str(content).split('>') if 'href' in e])
    sources = {
            e.replace('href="','')
                .replace('"><a','')
                .replace('">','')
                .replace('\\n','')
            for e in sources.split(' ') if 'href' in e}
    sources = [e if 'https' in e else base_path+e for e in sources]
    prof_sites = list({e for e in sources.split('"') if 'faculty-researchers' in e})
    return {'UT Austin CS':prof_sites}

def get_cu_cs_faculty(include_cv=False, only_cv=False):
    ''' Get Columbia CS faculty webpages'''
    base_path = get_cu_cs_base_path()
    print(f'Parsing: {base_path}')
    content = requests.get(base_path, timeout=10).content
    sources = '>'.join([e for e in str(content).split('>') if 'href' in e])
    sources = {
            e.replace('href=','')
                .replace('"','')
                .replace('<','')
                .replace('>','')
                .replace('\\n','')
                .replace('\\','')
            for e in sources.split(' ') if 'href' in e if '@' not in e}
    sources = [e for e in sources if '~' in e]
    if not include_cv or only_cv:
        sources = [e for e in sources if 'cv' not in e and 'CV' not in e]
    if only_cv:
        sources = [e for e in sources if 'cv' in e or 'CV' in e]

    return {'Columbia CS':sources}

def get_uta_cs_base_path():
    '''Get Columbia CS faculty base webpage'''
    return 'https://www.cs.utexas.edu/people'

def get_cu_cs_base_path():
    ''' Get Columbia CS faculty base webpage'''
    return 'https://www.cs.columbia.edu/people/faculty/'
