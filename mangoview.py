"""
Mango CLI Tools
Copyright (C) 2020 Alex Fence

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
import sys
import click
from mangofmt import MangoFile


@click.command()
@click.argument("file", nargs=1, required=True)
@click.argument("index", nargs=1, required=True)
def main(file, index):
    mangofile = MangoFile.open(file)

    try:
        index = int(index)
    except ValueError:
        exit(1)

    image = mangofile.get_image(index)

    if image.meta_data.compression is not None:
        image.uncompress()

    if image.meta_data.encryption is not None:
        exit(1)

    sys.stdout.buffer.write(image.image_data)


if __name__ == "__main__":
    main()
