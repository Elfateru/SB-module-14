class File:

    def __init__(self, file_name: str, mode: str) -> None:
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self) -> 'File':
        try:
            self.file = open(self.file_name, self.mode, encoding='utf-8')
        except Exception:
            self.file = open(self.file_name, 'a', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        return True


with File('example.txt', 'r') as file:
    print('Попробовали прочитать несуществующий файл')
