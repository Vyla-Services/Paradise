import struct

MAGIC = b"PARADISE"
VERSION = 1

ENTRY_HEADER_FMT = "<H"
ENTRY_META_FMT = "<BQQQ32s"
HEADER_FMT = "<8sII"

def write_index(f, entries):
    header = struct.pack(HEADER_FMT, MAGIC, VERSION, len(entries))
    f.write(header)
    for e in entries:
        path_bytes = e["path"].encode("utf-8")
        f.write(struct.pack(ENTRY_HEADER_FMT, len(path_bytes)))
        f.write(path_bytes)
        f.write(struct.pack(
            ENTRY_META_FMT,
            e["compression_id"],
            e["offset"],
            e["size_raw"],
            e["size_comp"],
            e["hash"],
        ))

def read_index(f):
    header_bytes = f.read(struct.calcsize(HEADER_FMT))
    if len(header_bytes) != struct.calcsize(HEADER_FMT):
        raise ValueError("Corrupt header")
    magic, version, count = struct.unpack(HEADER_FMT, header_bytes)
    if magic != MAGIC:
        raise ValueError("Invalid magic")
    if version != VERSION:
        raise ValueError("Unsupported version")
    entries = []
    for _ in range(count):
        name_len_bytes = f.read(struct.calcsize(ENTRY_HEADER_FMT))
        if len(name_len_bytes) != struct.calcsize(ENTRY_HEADER_FMT):
            raise ValueError("Corrupt entry header")
        name_len = struct.unpack(ENTRY_HEADER_FMT, name_len_bytes)[0]
        name = f.read(name_len).decode("utf-8")
        meta_bytes = f.read(struct.calcsize(ENTRY_META_FMT))
        if len(meta_bytes) != struct.calcsize(ENTRY_META_FMT):
            raise ValueError("Corrupt entry meta")
        compression_id, offset, size_raw, size_comp, h = struct.unpack(ENTRY_META_FMT, meta_bytes)
        entries.append({
            "path": name,
            "compression_id": compression_id,
            "offset": offset,
            "size_raw": size_raw,
            "size_comp": size_comp,
            "hash": h,
        })
    data_start = f.tell()
    return entries, data_start
