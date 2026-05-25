from .zlib_backend import ZlibBackend

try:
    from .lz4_backend import Lz4Backend
except ImportError:
    Lz4Backend = None

try:
    from .zstd_backend import ZstdBackend
except ImportError:
    ZstdBackend = None

BACKENDS = {
    "zlib": ZlibBackend,
    "lz4": Lz4Backend,
    "zstd": ZstdBackend,
}

def get_backend(name):
    backend_cls = BACKENDS.get(name)
    if backend_cls is None:
        raise ValueError(f"Compression backend not available: {name}")
    return backend_cls()
