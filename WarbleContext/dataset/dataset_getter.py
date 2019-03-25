import glob

from WarbleContext import settings
from WarbleContext.dataset.dataset_downloader import URLDownloader
from WarbleContext.dataset.dataset_extractor import ZipExtractor
from WarbleContext.dataset.source_parser import CasasParser

if __name__ == '__main__':
    # SOURCE PARSER
    sources = list()
    sources.append({
        'source': 'casas',
        'datasets': CasasParser('http://casas.wsu.edu/datasets/').execute(),
    })
    # sources.append({
    #     'source': 'A4H',
    #     'datasets': A4HParser(
    #         'https://data.mendeley.com/datasets/fcj2hmz5kb/3#folder-b0444e4a-ba47-467e-8ec2-0b9e5c4dfc1f').parse(),
    # })
    # END of SOURCE PARSER

    # DOWNLOADER
    for source in sources:
        for dataset in source['datasets']:
            urldownloader = URLDownloader(dataset['url'])
            urldownloader.execute()
    # END of DOWNLOADER

    # EXTRACTOR
    zip_files = glob.glob(settings.RAW_OUTPUT_PATH + '/*.zip')
    for file in zip_files:
        zip_extractor = ZipExtractor(file)
        zip_extractor.execute()
    # END of EXTRACTOR
