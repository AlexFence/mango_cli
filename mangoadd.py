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
import os
import click
from mangofmt import MangoFile
from mangofmt.error import WriteError


@click.command()
@click.argument("filename")
@click.argument("image")
def main(filename, image):
    if not os.path.isfile(filename):
        click.echo("{} does not exist.".format(filename))
        exit(1)

    if not os.path.isfile(image):
        click.echo("{} does not exist.".format(image))
        exit(1)

    file = MangoFile.open(filename)

    file.add_image_by_path(image)

    try:
        file.save(filename)
        exit(0)
    except WriteError:
        click.echo("WriteError: could not save" + filename)
        exit(3)
    except PermissionError:
        click.echo("Permission denied: could not save" + filename)
        exit(4)


if __name__ == "__main__":
    main()
    main()
