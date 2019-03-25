import os

import requests

import settings
from dataset.source_parser import CasasParser, A4HParser


class Downloader:
    def __init__(self):
        pass


class URLDownloader(Downloader):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def is_url_downloadable(self):
        h = requests.head(self.url, allow_redirects=True)
        header = h.headers
        content_type = header.get('content-type')
        if 'text' in content_type.lower():
            return False
        if 'html' in content_type.lower():
            return False
        return True

    def download(self):
        if self.is_url_downloadable():
            r = requests.get(self.url, allow_redirects=True)
            open(os.path.join(settings.RAW_OUTPUT_PATH, self.url.split('/')[-1]), 'wb').write(r.content)


if __name__ == '__main__':
    sources = list()
    sources.append({
        'source': 'casas',
        'datasets': CasasParser('http://casas.wsu.edu/datasets/').parse(),
    })
    # sources.append({
    #     'source': 'A4H',
    #     'datasets': A4HParser(
    #         'https://data.mendeley.com/datasets/fcj2hmz5kb/3#folder-b0444e4a-ba47-467e-8ec2-0b9e5c4dfc1f').parse(),
    # })

    for source in sources:
        for dataset in source['datasets']:
            urldownloader = URLDownloader(dataset['url'])
            urldownloader.download()
