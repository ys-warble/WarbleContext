import zipfile


class Extractor:
    pass


class ZipExtractor:
    def __init__(self, input_path, output_path=None):
        self.input_path = input_path
        if output_path is None:
            self.output_path = self.input_path.replace('.zip', '')
        else:
            self.output_path = output_path

    def extract(self):
        print('Extracting %s' % self.input_path)
        zip_ref = zipfile.ZipFile(self.input_path, 'r')
        zip_ref.extractall(self.output_path)
        zip_ref.close()


if __name__ == '__main__':
    pass
