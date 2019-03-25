import requests
from bs4 import BeautifulSoup
import pprint


class SourceParser:
    pass


class CasasParser(SourceParser):
    def __init__(self, url):
        self.url = url

    def parse(self):
        r = requests.get(self.url, allow_redirects=True)
        soup = BeautifulSoup(r.text, 'html.parser')

        tbody = soup.find('div', {'class': ['entry-content', 'clear-fix']}).find('table').find('tbody')
        trs = tbody.find_all('tr')

        result = list()
        for tr in trs:
            tds = tr.find_all('td')

            if tds[0].a is None:
                continue

            url = tds[0].a['href']
            seq_no = tds[0].a.getText()
            testbed = tds[1].getText()
            no_residence = tds[2].getText()
            description = tds[3].getText()
            annotated = tds[4].getText()
            last_updated = tds[5].getText()

            result.append({
                'seq_no': seq_no,
                'url': url,
                'testbed': testbed,
                'no_residence': no_residence,
                'description': description,
                'annotated': annotated,
                'last_updated': last_updated,
            })

        return result


class A4HParser(SourceParser):
    def __init__(self, url):
        self.url = url

    def parse(self):
        r = requests.get(self.url, allow_redirects=True)
        soup = BeautifulSoup(r.text, 'html.parser')
        result = list()

        div_url = soup.find('div', attrs={'class': 'filelist-toolbar-right'})
        url = 'https://' + self.url.split('/')[2] + div_url.a['href']

        p_last_updated = soup.find('p', attrs={'class': 'versionlist-version-posted'})
        last_updated = p_last_updated.getText()

        result.append({
            'seq_no': None,
            'url': url,
            'testbed': None,
            'no_residence': None,
            'description': None,
            'annotated': None,
            'last_updated': last_updated,
        })

        return result


if __name__ == '__main__':
    source = dict()
    # casas_parser = CasasParser('http://casas.wsu.edu/datasets/')
    # source['source'] = 'casas'
    # source['datasets'] = casas_parser.parse()

    a4h_parser = A4HParser('https://data.mendeley.com/datasets/fcj2hmz5kb/3#folder-b0444e4a-ba47-467e-8ec2-0b9e5c4dfc1f')
    source['source'] = 'A4H'
    source['datasets'] = a4h_parser.parse()

    pprint.pprint(source)
