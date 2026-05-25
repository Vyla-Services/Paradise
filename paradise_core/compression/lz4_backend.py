import lz4.frame

class Lz4Backend:
    name = "lz4"
    id = 2

    def compress(self, data, level=0):
        return lz4.frame.compress(data, compression_level=level)

    def decompress(self, data):
        return lz4.frame.decompress(data)
