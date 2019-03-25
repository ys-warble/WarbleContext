import os
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
        if os.path.exists(self.output_path) and len(os.listdir(self.output_path)) != 0:
            print('Skipping \'%s\': not empty' % os.path.basename(self.input_path))
        else:
            print('Extracting \'%s\' ...' % os.path.basename(self.input_path))
            zip_ref = zipfile.ZipFile(self.input_path, 'r')
            zip_ref.extractall(self.output_path)
            zip_ref.close()


if __name__ == '__main__':
    pass
