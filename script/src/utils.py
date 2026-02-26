# pyright: basic
from argparse import Namespace, ArgumentParser
from os import makedirs
from os.path import dirname, exists, abspath
from shutil import rmtree

def liner() -> Namespace:
    """
    Parses the command line input
    ----------
    Returns:
        cmd: Namespace, A namespace object with all possible commands
    """
    prs: ArgumentParser = ArgumentParser(
        prog = '',
        description = '',
        epilog = 'Work in progress'
    )
    py: str = abspath(dirname(__file__)) + '/'
    source: str = abspath(dirname(dirname(__file__))) + '/'
    general = prs.add_argument_group('General')
    _ = general.add_argument(
        "-v",
        "--verbose",
        help = "Prints more while running",
        dest='verbose',
        type = str,
    )
    _ = general.add_argument(
        "--version",
        help = """Prints the program version""",
        dest="ver",
        action="version",
        version="%(prog)s 0.1.3",
    )
    _ = general.add_argument(
        "-d",
        "--defaults",
        help = "Prints argument defaults",
        action = 'store_true',
        default=False,
        dest='default',
    )
    _ = general.add_argument(
        "-o",
        "--output",
        help = "Define the folder you want the output in",
        default= source + 'output/',
        dest='output',
        type = str,
    )
    _ = general.add_argument(
        "-clear",
        "--clearFirst",
        help = """Clears the output folders before executing (Note this is deprecated and will remove the output directory multiple times in a run thus it won't work. It was only for testing the building of the project no more than that)""",
        action="store_true",
        default=False,
        dest="clear",
    )
    cmd: Namespace = prs.parse_args()
    if cmd.default:
        for args, value in vars(cmd).items():
            print(f'{args}: {value}')
        exit('Defaults printed, exiting')
    makedirs(cmd.output, exist_ok=True)
    if cmd.clear:
        if exists(cmd.output):
            confirm: str = input(f'Are you sure you want to remove {cmd.output}? [y/N]')
            if confirm.lower() == 'y':
                rmtree(cmd.output)  # Surely nothing bad will come of this
            else:
                exit('Broke before clearing output for safety')
    return cmd

if __name__ == "__main__":
    cmd: Namespace = liner()
