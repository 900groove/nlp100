def task00(s):
    return ''.join(reversed(s))


def test_task00(s='stressed'):
    assert 'desserts' == task00(s)


def task01(s):
    return ''.join([w for n, w in enumerate(s) if n % 2 != 0])


def test_task01(s='パタトクカシーー'):
    assert 'タクシー' == task01(s)


def task02(s1, s2):
    return ''.join([_s1 + _s2 for _s1, _s2 in zip(s1, s2)])


def test_task02(s1='パトカー', s2='タクシー'):
    assert 'パタトクカシーー' == task02(s1, s2)


def task03(sent):
    return sorted(sent.split(), key=lambda x: len(x))


def test_task03():
    sent = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    words = task03(sent)
    for n in range(1, len(words)):
        assert len(words[n - 1]) <= len(words[n])


def task04(sent):
    index_loc = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    output = {}
    for n, w in enumerate(sent.split()):
        if n in index_loc:
            output[w[:1]] = n
        else:
            output[w[:2]] = n
    return output


def test_task04():
    sent = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    sent_index = task04(sent)
    assert sent_index['H'] == 1
    assert sent_index['Hi'] == 0


def task05(sent):
    words = sent.split()
    word_2gram = [' '.join([words[n], words[n + 1]]) for n in range(len(words) - 1)]
    char_2gram = [' '.join([sent[n], sent[n + 1]]) for n in range(len(sent) - 1)]
    return word_2gram, char_2gram


def test_task05():
    sent = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    word_2gram, char_2gram = task05(sent)
    assert word_2gram[0] == 'Hi He'
    assert word_2gram[1] == 'He Lied'
    assert char_2gram[0] == 'H i'
    assert char_2gram[1] == 'i  '


def task06(x='paraparaparadise', y='paragraph'):
    X = set([x[n] + x[n + 1] for n in range(len(x) - 1)])
    Y = set([y[n] + y[n + 1] for n in range(len(y) - 1)])
    return X | Y, X ^ Y, 'se' in X, 'se' in Y


def test_task06():
    or_set, not_set, x_result, y_result = task06()
    assert 'pa' in or_set
    assert 'ph' in not_set
    assert x_result is True
    assert y_result is False


def task07(x=12, y='気温', z=22.4):
    return f"{x}時の{y}は{z}"


def test_task07():
    assert task07() == "12時の気温は22.4"


def task08(s):
    return ''.join([chr(219 - ord(w)) if w.islower() else w for w in s])


def test_task08():
    assert r'svLLl' == task08('heLLo')


def task09(sent):
    from random import sample
    output = []
    for w in sent.split():
        if len(w) <= 4:
            output.append(w)
        else:
            output.append(w[0] + ''.join(sample(w[1: -1], len(w) - 2)) + w[-1])
    return ' '.join(output)


def test_task09():
    sent = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    sent_after = task09(sent)
    assert sent_after.split()[0] == 'I'
    assert sent_after.split()[1] != "couldn't"
    assert sent_after.split()[1][0] == 'c'
    assert sent_after.split()[1][-1] == 't'
