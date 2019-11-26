from os import remove
from time import sleep
from os.path import exists
from json import dump, load

class Helper:
    def __init__(self, url: str, base_dir: str):
        self.url = url
        self.base_dir = base_dir

    def handle_error(self, e: Exception, message: str = 'Error Occured'):
        print(e, message)

    def get_url(self) -> str:
        try:
            return self.url
        except Exception as e:
            self.handle_error(e, 'Error occured during login')

    def write_file(self, *args) -> None:
        try:
            file_data: set = args[0]
            file_name: str = args[1]

            file_path: str = f'{self.base_dir}/{file_name}'
            path_exists = exists(file_path)

            file_ctx = open(
                file_path, 'r+') if path_exists else open(file_path, 'w+')

            if not path_exists:
                dump(file_data, file_ctx, indent=4)
            else:
                remove(file_path)
                self.write_file(file_data, file_name)

        except Exception as e:
            self.handle_error(e, 'Error occured while writing to file')

    def duration(self, seconds: int = 0) -> None:
        try:
            return sleep(seconds)
        except Exception as e:
            self.handle_error(e, 'Error occured in chrome driver duration')
