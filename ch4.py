def task31():
    with open('data/nelo.txt.mecab', 'r') as f:
        data = f.read()
        for l in data.split('\n'):

            if l == 'EOS' or l == '':
                continue
            surface, tag = l.split('\t')
            tags = tag.split(',')
            yield {
                "surface": surface,
                "base": tags[6],
                "pos": tags[0],
                "pos1": tags[1]
            }


def test_task31():
    assert next(task31()) == {'surface': '一', 'base': '一', 'pos': '名詞', 'pos1': '数'}


def task32():
    return [t['surface'] for t in task31() if t['pos'] == '動詞']


def test_task32():
    verbs = task32()
    for w in list('がのをに'):
        assert w not in verbs


def task33():
    return [t['surface'] for t in task31() if 'サ変接続' in t['pos1']]


def test_task33():
    assert len(task33()) == 5209


def task34():
    tokens = list(task31())
    for idx in range(1, len(tokens)):
        if tokens[idx - 1]["pos"] == '名詞' and tokens[idx]['surface'] == 'の' and tokens[idx + 1]['pos'] == '名詞':
            yield (tokens[idx - 1]['surface'] + tokens[idx]['surface'] + tokens[idx + 1]['surface'])


def test_task34():
    for span in task34():
        assert 'の' in span


def task35():
    max_span = []
    span = []
    tokens = list(task31())
    for idx in range(1, len(tokens)):
        if tokens[idx - 1]['pos'] == '名詞' and tokens[idx]['pos'] == '名詞':
            if len(span) == 0:
                span.append(tokens[idx - 1]['surface'])
            span.append(tokens[idx]['surface'])
            if len(span) > len(max_span):
                max_span = span
        else:
            span = []

    return max_span


def test_task35():
    assert len(task35()) == 10


def task36():
    from collections import Counter
    words = [w['surface'] for w in task31()]
    c = Counter(words)
    return c.most_common()


def test_task36():
    most_common = task36()[:3]
    for true, ans in zip(['の', '。', 'て'], most_common):
        assert true == ans[0]


def task37():
    import matplotlib.pyplot as plt
    import japanize_matplotlib
    common = task36()[:10]
    plt.bar([c[0] for c in common], [c[1] for c in common])
    plt.savefig('data/common.png')


def test_task37():
    task37()
    import glob
    assert 'data/common.png' in glob.glob('data/*.png')


def task38():
    import matplotlib.pyplot as plt
    import japanize_matplotlib
    common = task36()
    common = [c[1] for c in common]
    plt.hist(common, 100)
    plt.xlabel('出現頻度')
    plt.ylabel('語彙数')
    plt.savefig('data/common_freq.png')


def test_task38():
    task38()
    import glob
    assert 'data/common_freq.png' in glob.glob('data/*png')


def task39():
    import math
    import matplotlib.pyplot as plt
    import japanize_matplotlib
    common = task36()
    freq = [math.log(c[1]) for c in common]
    plt.bar([math.log(i) for i in range(1, len(freq) + 1)], freq)
    plt.savefig('data/ziph.png')


def test_task39():
    task39()
    import glob
    assert 'data/ziph.png' in glob.glob('data/*png')


if __name__ == '__main__':
    task39()