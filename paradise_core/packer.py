import os
from .utils import walk_files, logger
from .compression import get_backend
from .crypto import sha256_bytes
from .index import write_index

def pack_folder(input_dir, output_pak, compression="zlib", level=9):
    backend = get_backend(compression)
    files = list(walk_files(input_dir))
    entries = []
    data_chunks = []
    offset = 0
    for rel, full in files:
        with open(full, "rb") as f:
            raw = f.read()
        comp = backend.compress(raw, level) if hasattr(backend, "compress") and "level" in backend.compress.__code__.co_varnames else backend.compress(raw)
        h = sha256_bytes(raw)
        entry = {
            "path": rel,
            "compression_id": backend.id,
            "offset": offset,
            "size_raw": len(raw),
            "size_comp": len(comp),
            "hash": h,
        }
        entries.append(entry)
        data_chunks.append(comp)
        offset += len(comp)
    with open(output_pak, "wb") as out:
        write_index(out, entries)
        for chunk in data_chunks:
            out.write(chunk)
    logger.info(f"Packed {len(entries)} files into {os.path.basename(output_pak)}")
