from paradise_core.index import read_index

def cmd_list(args):
    with open(args.pak_path, "rb") as f:
        entries, _ = read_index(f)
        for e in entries:
            print(e["path"], e["size_raw"], e["size_comp"])
