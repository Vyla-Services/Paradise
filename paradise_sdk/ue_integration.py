import os
from .reader import ParadiseReader

class UEParadiseBridge:
    def __init__(self, pak_path):
        self.reader = ParadiseReader(pak_path)

    def export_to_content(self, ue_content_dir):
        for path in self.reader.list_files():
            data = self.reader.read_file(path)
            out_path = os.path.join(ue_content_dir, path)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "wb") as f:
                f.write(data)

    def get_asset_bytes(self, asset_path):
        return self.reader.read_file(asset_path)

    def mount_virtual(self):
        return self.reader.list_files()
