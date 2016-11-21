from bs4 import BeautifulSoup
from os import walk
from os.path import join
from json import dump



def append_all(rows, low_words):
    if rows[2].get_text()=='example sentence':
        low_words[rows[1].get_text()].append(rows[3].get_text().replace('"', ''))
    else:
        for tokens in rows[3].get_text().split(';'):
            low_words[rows[1].get_text()].append(tokens.replace('"', ''))
    return None


def init_all(rows, luluaoe):
    if rows[2].get_text()=='example sentence':
        luluaoe[rows[1].get_text()]=[rows[3].get_text().replace('"', '')]
    else:
        luluaoe[rows[1].get_text()]=rows[3].get_text().replace('"', '').split(';')
    return None


def extract(path):
    with open(path, 'r') as f:
        rows = ''
        soup = BeautifulSoup(f, 'html.parser',from_encoding='utf-8')
        table = soup.find_all(attrs={"class":"gridtable"})[0]
        for row in table.find_all('tr'):
            if len(row.find_all('td'))==2:
                words[rows[1].get_text()].append(row.find_all('td')[1].get_text().replace('"', ''))
                continue
            rows = row.find_all('td')
            try:
                try:
                    append_all(rows,words)
                except KeyError:
                    init_all(rows,words)
            except IndexError:
                continue


words_reversed={}
def new_extract(path):
    with open(path, 'r') as f:
        rows = ''
        soup = BeautifulSoup(f, 'html.parser',from_encoding='utf-8')
        table = soup.find_all(attrs={"class":"gridtable"})[0]
        for row in table.find_all('tr'):
            if len(row.find_all('td'))==2:
                for tokens in row.find_all('td')[1].get_text().split(';'):
                    try:
                        words_reversed[tokens.replace('"', '')].append(rows[1].get_text())
                    except KeyError:
                        words_reversed[tokens.replace('"', '')]=[rows[1].get_text()]
                    continue
            rows = row.find_all('td')
            try:
                append_all_rev(rows,words_reversed)
            except IndexError:
                continue


def append_all_rev(rows, wordshehe):
    try:
        if rows[2].get_text()=='example sentence':
            wordshehe[rows[3].get_text().replace('"', '')].append(rows[1].get_text())
        else:
            for tokens in rows[3].get_text().split(';'):
                wordshehe[tokens.replace('"', '')].append(rows[1].get_text())
        return None
    except KeyError:
        if rows[2].get_text()=='example sentence':
            wordshehe[rows[3].get_text().replace('"', '')]=[rows[1].get_text()]
        else:
            for tokens in rows[3].get_text().split(';'):
                wordshehe[tokens.replace('"', '')]=[rows[1].get_text()]
        return None


def dump_dict(wordsullu,name):
    with open(name+'.json', 'w') as f:
        dump(wordsullu,f, ensure_ascii=False)




if __name__ == '__main__':
    words={}
    words_reversed={}
    for root, dirs, files in walk('/Users/gaurwaithmelui/PycharmProjects/english_thai_dict/thai_pages'):
        for file in files:
            filepath=join(root,file)
            extract(filepath)
            new_extract(filepath)

    dump_dict(words, 'thai_to_english')
    dump_dict(words_reversed, 'english_to_thai')
