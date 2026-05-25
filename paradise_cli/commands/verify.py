from paradise_core.index import read_index
from paradise_core.crypto import sha256_bytes
from paradise_core.compression import ZlibBackend, Lz4Backend, ZstdBackend

BACKENDS = {
    1: ZlibBackend,
    2: Lz4Backend,
    3: ZstdBackend,
}

def cmd_verify(args):
    with open(args.pak_path, "rb") as f:
        entries, data_start = read_index(f)
        for e in entries:
            backend_cls = BACKENDS.get(e["compression_id"])
            backend = backend_cls()
            f.seek(data_start + e["offset"])
            comp = f.read(e["size_comp"])
            raw = backend.decompress(comp)
            if sha256_bytes(raw) != e["hash"]:
                print("FAIL", e["path"])
                return
        print("OK")
