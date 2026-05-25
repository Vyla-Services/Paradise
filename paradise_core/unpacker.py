from .compression import ZlibBackend, Lz4Backend, ZstdBackend
from .crypto import sha256_bytes
from .index import read_index
from .utils import logger
import os

BACKEND_BY_ID = {
    1: ZlibBackend,
    2: Lz4Backend,
    3: ZstdBackend,
}

def extract_pak(pak_path, output_dir):
    with open(pak_path, "rb") as f:
        entries, data_start = read_index(f)
        for e in entries:
            backend_cls = BACKEND_BY_ID.get(e["compression_id"])
            if backend_cls is None:
                raise ValueError(f"Unknown compression id {e['compression_id']}")
            backend = backend_cls()
            f.seek(data_start + e["offset"])
            comp = f.read(e["size_comp"])
            raw = backend.decompress(comp)
            if len(raw) != e["size_raw"]:
                raise ValueError("Size mismatch")
            if sha256_bytes(raw) != e["hash"]:
                raise ValueError("Hash mismatch")
            out_path = os.path.join(output_dir, e["path"])
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "wb") as out:
                out.write(raw)
    logger.info(f"Extracted {len(entries)} files from {os.path.basename(pak_path)}")
