from paradise_core import pack_folder

def cmd_pack(args):
    pack_folder(args.input_dir, args.output_pak, args.compression, args.level)
