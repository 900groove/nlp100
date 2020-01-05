import re
import json


def parse_json():
    with open('data/jawiki-country.json', 'r') as f:
        for line in f:
            yield json.loads(line)


def task20():
    for line in parse_json():
        if re.search('イギリス', line['title']):
            return line['text']


def test_task20():
    text = task20()
    assert re.search('略名 = イギリス', text[:100])


def task21():
    text = task20()
    for line in text.split('\n'):
        if re.search('Category:', line):
            yield line


def test_task21():
    for line in task21():
        assert 'Category:' in line


def task22():
    text = task20()
    for line in text.split('\n'):
        if re.search(r"Category:(.*?)(\|.*?)?\]\]", line):
            yield line[line.index(':') + 1: line.index(']]')]


def test_task22():
    result = list(task21())
    assert len(result) == 8


def task23():
    text = task20()
    for line in text.split('\n'):
        if re.search('^(=+).{,20}(=+)$', line):
            yield re.sub('=', '', line), line.count('=') / 2 - 1


def test_task23():
    sections = list(task23())
    assert ('映画', 2.0) in sections
    assert ('文化', 1.0) in sections


def task24():
    text = task20()
    for line in text.split('\n'):
        m = re.search(r"(ファイル|File):(.+?)\|", line)
        if m:
            yield m.group()


def test_task24():
    files = list(task24())
    assert len(files) == 34


def task25():
    text = task20()
    span = {}
    span_start, span_end = False, False
    for line in text.split('\n'):
        if re.search(r'\{\{基礎情報 ', line):
            span_start = True
        if re.match(r'^\}\}$', line):
            span_end = True
        if span_start is True and span_end is False:
            if re.match(r'\|.*?', line):
                key = line.split(' ')[0][1:]
                value = line[line.index('= ') + 2:]
                span[key] = value
    return span


def test_task25():
    info = task25()
    assert type(info) is dict
    assert len(info) > 1
    assert info['略名'] == 'イギリス'


def task26():
    info = task25()
    for key in info:
        info[key] = info[key].replace("'''''", '').replace("'''", '').replace("''", '')
    return info


def test_task26():
    before = task25()
    after = task26()
    assert before['確立形態4'] != after['確立形態4']
    assert "'" not in after['確立形態4']


def task27():
    info = task25()
    p = r"\[\[.*?\]\]"
    for key in info:
        value = info[key]
        match = re.findall(p, value)
        for m in match:
            if m:
                norm = re.sub(r'(\[\[)|(\]\])', '', m).split('|')[-1]
                value = value.replace(m, norm)
        info[key] = value
    return info


def test_task27():
    info = task27()
    for k in info:
        assert '[[' not in info[k]


def task28():
    info = task27()
    p = r"\{\{.*?\}\}"
    for k in info:
        value = info[k]
        value = re.sub(r'\<.*?\>.*?\</.*?\>', '', value)
        value = re.sub(r'\<.*?\>', '', value)
        value = re.sub(r'\'{2,}', '', value)
        match = re.findall(p, value)
        for m in match:
            if m:
                norm = re.sub(r'(\{\{)|(\}\})', '', m).split('|')[-1]
                value = value.replace(m, norm)
        info[k] = value
    return info


def test_task28():
    info = task28()
    symbols = ["'''", "<ref>", "<br>", "[["]
    for k in info:
        for s in symbols:
            assert s not in info[k]


def task29():
    """ run
    GET https://ja.wikipedia.org/w/api.php?action=query&format=json&prop=imageinfo&titles=File:Flag%20of%20the%20United%20Kingdom.svg&iiprop=url
    """
    response = \
        {
            "continue": {
                "iistart": "2007-09-03T09:51:34Z",
                "continue": "||"
            },
            "query": {
                "normalized": [
                    {
                        "from": "File:Flag of the United Kingdom.svg",
                        "to": "\u30d5\u30a1\u30a4\u30eb:Flag of the United Kingdom.svg"
                    }
                ],
                "pages": {
                    "-1": {
                        "ns": 6,
                        "title": "\u30d5\u30a1\u30a4\u30eb:Flag of the United Kingdom.svg",
                        "missing": "",
                        "known": "",
                        "imagerepository": "shared",
                        "imageinfo": [
                            {
                                "url": "https://upload.wikimedia.org/wikipedia/commons/a/ae/Flag_of_the_United_Kingdom.svg",
                                "descriptionurl": "https://commons.wikimedia.org/wiki/File:Flag_of_the_United_Kingdom.svg",
                                "descriptionshorturl": "https://commons.wikimedia.org/w/index.php?curid=347935"
                            }
                        ]
                    }
                }
            }
        }

    result = response['query']['pages']['-1']['imageinfo'][0]['url']
    return result


def test_task29():
    result = task29()
    assert result == 'https://upload.wikimedia.org/wikipedia/commons/a/ae/Flag_of_the_United_Kingdom.svg'
