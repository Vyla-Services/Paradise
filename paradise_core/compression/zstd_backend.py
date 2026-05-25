import zstandard as zstd

class ZstdBackend:
    name = "zstd"
    id = 3

    def __init__(self, level=10):
        self._cctx = zstd.ZstdCompressor(level=level)
        self._dctx = zstd.ZstdDecompressor()

    def compress(self, data):
        return self._cctx.compress(data)

    def decompress(self, data):
        return self._dctx.decompress(data)
