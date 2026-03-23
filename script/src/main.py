"""

"""
# pyright: basic
from argparse import Namespace
from utils import liner # Won't error

def main() -> None:
    """
    Documentation
    ----------
    Arguments:
        arg: type
    ----------
    Returns:
        output: None
    """
    cmd: Namespace = liner()

if __name__ == "__main__":
    main()
