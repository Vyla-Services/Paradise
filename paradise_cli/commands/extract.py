from paradise_core import extract_pak

def cmd_extract(args):
    extract_pak(args.pak_path, args.output_dir)
