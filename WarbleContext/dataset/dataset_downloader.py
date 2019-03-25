import os

import requests

from WarbleContext import settings
from WarbleContext.dataset.source_parser import CasasParser


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

    def download(self, directory=None):
        file_name = self.url.split('/')[-1]
        if directory is None:
            output_path = os.path.join(settings.RAW_OUTPUT_PATH, file_name)
        else:
            output_path = directory

        if not self.is_url_downloadable():
            print('Skipping \'%s\': not downloadable' % file_name)
        elif os.path.exists(output_path):
            print('Skipping \'%s\': already exist' % file_name)
        else:
            print('Downloading \'%s\' ...' % file_name)
            r = requests.get(self.url, allow_redirects=True)
            open(output_path, 'wb').write(r.content)


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
