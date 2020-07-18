#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Program description goes here."""
import argparse
import sys
from typing import Optional, Sequence, Union

__author__ = 'Sergey M <tz4678@gmail.com>'
__version__ = '0.1.0'


def main(argv: Optional[Sequence[str]] = None) -> Union[None, int, str]:
    """Main function."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-v', '--version', action='version', version=f'v{__version__}'
    )
    args = parser.parse_args(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
