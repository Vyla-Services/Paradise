from .reader import ParadiseReader

class ParadiseLoader:
    def __init__(self, pak_path):
        self.reader = ParadiseReader(pak_path)

    def load_text(self, path):
        data = self.reader.read_file(path)
        if data is None:
            return None
        return data.decode("utf-8", errors="ignore")

    def load_binary(self, path):
        return self.reader.read_file(path)

    def load_json(self, path):
        data = self.load_text(path)
        if data is None:
            return None
        import json
        return json.loads(data)
