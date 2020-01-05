import subprocess


def task10():
    args = ['wc', 'data/hightemp.txt']
    res = subprocess.check_output(args)
    return int(res.split()[0])


def test_task10():
    assert task10() == 24


def task11():
    command = "cat data/hightemp.txt | sed -e 's/\t/ /g' > data/hightemp2.txt"
    subprocess.run(command, shell=True)


def test_task11():
    task11()
    with open('data/hightemp2.txt', 'r') as f:
        file = f.read()
    for line in file:
        assert r'\t' not in line


def task12():
    first_col = 'cut -f 1 -d " " data/hightemp2.txt > data/col1.txt'
    second_col = 'cut -f 2 -d " " data/hightemp2.txt > data/col2.txt'
    subprocess.run(first_col, shell=True)
    subprocess.run(second_col, shell=True)


def test_task12():
    task12()
    with open('data/col1.txt', 'r') as f:
        f1 = f.read()
        assert f1.split('\n')[0] == '高知県'

    with open('data/col2.txt', 'r') as f:
        f2 = f.read()
        assert f2.split('\n')[0] == '江川崎'


def task13():
    command = 'paste data/col1.txt data/col2.txt > data/concat_col.txt'
    subprocess.run(command, shell=True)


def test_task13():
    task13()
    with open('data/concat_col.txt', 'r') as f:
        data = f.read()
        assert data.split('\n')[0] == '高知県\t江川崎'


def task14(n=3):
    command = f'head -n{n} data/hightemp.txt'
    res = subprocess.check_output(command, shell=True)
    return res.decode()


def test_task14():
    res = task14().split('\n')
    assert res[0] == '高知県\t江川崎\t41\t2013-08-12'


def task15(n=3):
    command = f'tail -n{n} data/hightemp.txt'
    res = subprocess.check_output(command, shell=True)
    return res.decode()


def test_task15():
    res = task15().split('\n')
    assert res[-2] == '愛知県\t名古屋\t39.9\t1942-08-02'


def task16(n=2):
    count = subprocess.check_output('wc data/hightemp.txt', shell=True).split()[0]
    split_size = int(count) // n
    command = f'split -l {split_size} -d data/hightemp.txt data/split-'
    subprocess.run(command, shell=True)


def test_task16():
    task16()
    assert len(subprocess.check_output('find data/split*', shell=True).split()) == 2


def task17():
    line = subprocess.check_output('head -n1 data/hightemp.txt', shell=True).decode()
    return set(list(line))


def test_task17():
    res = task17()
    for c in list('高知県'):
        assert c in res


def task18():
    command = 'sort -k 2 -t " " data/hightemp2.txt '
    res = subprocess.check_output(command, shell=True).decode()
    return res


def test_task18():
    res = task18()
    for ans, line in zip(['和歌山県', '群馬県', '静岡県'], res.split('\n')[:3]):
        assert ans == line.split()[0]


def task19():
    command = 'cut -f 1 -d " " data/hightemp2.txt | sort | uniq -c | sort -nr'
    res = subprocess.check_output(command, shell=True).decode()
    return res


def test_task19():
    res = task19()
    ans = ['群馬県', '山形県', '山梨県', '埼玉県']
    for data in res.split('\n')[:4]:
        assert data.split()[1] in ans


if __name__ == '__main__':
    print(task17())
