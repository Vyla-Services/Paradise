import os
from .reader import ParadiseReader

class OGFNParadiseIntegration:
    def __init__(self, pak_path):
        self.reader = ParadiseReader(pak_path)

    def get_manifest(self):
        if "manifest.json" in self.reader.list_files():
            return self.reader.read_file("manifest.json")
        return None

    def stream_asset(self, path):
        return self.reader.read_file(path)

    def extract_all(self, output_dir):
        for path in self.reader.list_files():
            data = self.reader.read_file(path)
            out_path = os.path.join(output_dir, path)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "wb") as f:
                f.write(data)
