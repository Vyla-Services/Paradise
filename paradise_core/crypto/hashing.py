import hashlib

def sha256_bytes(data):
    h = hashlib.sha256()
    h.update(data)
    return h.digest()
