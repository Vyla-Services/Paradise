import argparse
from .commands.pack import cmd_pack
from .commands.extract import cmd_extract
from .commands.list import cmd_list
from .commands.verify import cmd_verify

def main():
    parser = argparse.ArgumentParser(prog="paradise")
    sub = parser.add_subparsers(dest="command")

    p_pack = sub.add_parser("pack")
    p_pack.add_argument("input_dir")
    p_pack.add_argument("output_pak")
    p_pack.add_argument("--compression", default="zlib")
    p_pack.add_argument("--level", type=int, default=9)

    p_extract = sub.add_parser("extract")
    p_extract.add_argument("pak_path")
    p_extract.add_argument("output_dir")

    p_list = sub.add_parser("list")
    p_list.add_argument("pak_path")

    p_verify = sub.add_parser("verify")
    p_verify.add_argument("pak_path")

    args = parser.parse_args()

    if args.command == "pack":
        cmd_pack(args)
    elif args.command == "extract":
        cmd_extract(args)
    elif args.command == "list":
        cmd_list(args)
    elif args.command == "verify":
        cmd_verify(args)
    else:
        parser.print_help()
