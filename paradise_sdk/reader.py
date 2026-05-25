import os
from paradise_core.index import read_index
from paradise_core.compression import ZlibBackend, Lz4Backend, ZstdBackend

BACKENDS = {
    1: ZlibBackend,
    2: Lz4Backend,
    3: ZstdBackend,
}

class ParadiseReader:
    def __init__(self, pak_path):
        self.pak_path = pak_path
        self.entries = []
        self.data_start = 0
        self._load()

    def _load(self):
        with open(self.pak_path, "rb") as f:
            self.entries, self.data_start = read_index(f)

    def list_files(self):
        return [e["path"] for e in self.entries]

    def get_entry(self, path):
        for e in self.entries:
            if e["path"] == path:
                return e
        return None

    def read_file(self, path):
        e = self.get_entry(path)
        if not e:
            return None
        backend_cls = BACKENDS.get(e["compression_id"])
        backend = backend_cls()
        with open(self.pak_path, "rb") as f:
            f.seek(self.data_start + e["offset"])
            comp = f.read(e["size_comp"])
        return backend.decompress(comp)
