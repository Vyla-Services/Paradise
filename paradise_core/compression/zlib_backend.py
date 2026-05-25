import zlib

class ZlibBackend:
    name = "zlib"
    id = 1

    def compress(self, data, level=9):
        return zlib.compress(data, level)

    def decompress(self, data):
        return zlib.decompress(data)
