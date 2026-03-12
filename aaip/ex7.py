import argparse as ap
import shutil as sh
import os

# Copy File to one or more destinations
def copy_file(src, dst_list):
    try:
        for dst in dst_list:
            sh.copy(src, dst)
            print(f"File copied to {dst}")
    except FileNotFoundError:
        print(f"Error: The file '{src}' was not found.")
    except Exception as e:
        print(f"Error: {e}")

# Move File to Destination
def move_file(src, dst):
    try:
        sh.move(src, dst)
        print(f"File moved to {dst}")
    except FileNotFoundError:
        print(f"Error: The file '{src}' was not found.")
    except Exception as e:
        print(f"Error: {e}")

# Rename File
def rename_file(src, dst):
    try:
        os.rename(src, dst)
        print(f"File renamed to {dst}")
    except FileNotFoundError:
        print(f"Error: The file '{src}' was not found.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = ap.ArgumentParser(description="Copy, Move or Rename Files.")

    # Create subparsers
    subparsers = parser.add_subparsers(dest='command', help="Available commands")

    # Subcommand for copying files
    copy_parser = subparsers.add_parser('copy', help="Copy file to one or more destinations.")
    copy_parser.add_argument('--src', required=True, help="Source file to copy.")
    copy_parser.add_argument('--dst', nargs='+', required=True, help="One or more destination paths.")

    # Subcommand for moving files
    move_parser = subparsers.add_parser('move', help="Move a file to a new location.")
    move_parser.add_argument('--src', required=True, help="Source file to move.")
    move_parser.add_argument('--dst', required=True, help="Destination path.")

    # Subcommand for renaming files
    rename_parser = subparsers.add_parser('rename', help="Rename a file.")
    rename_parser.add_argument('--src', required=True, help="Current file name.")
    rename_parser.add_argument('--dst', required=True, help="New file name.")

    # Parse the arguments
    args = parser.parse_args()

    # Handle the different subcommands
    if args.command == 'copy':
        copy_file(args.src, args.dst)
    elif args.command == 'move':
        move_file(args.src, args.dst)
    elif args.command == 'rename':
        rename_file(args.src, args.dst)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

# python ex7.py copy --src ../demo7_copy.txt --dst copy1.txt ../copy2.txt
# python ex7.py move --dst demo7_move.txt --src ../demo7_move.txt
# python ex7.py rename --src ../demo7_rename.txt --dst ../demo7.txt