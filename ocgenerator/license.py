header_year = "2008-2016"
author = "Thomas Paviot"
author_email = "tpaviot@gmail.com"
license_header = """
This file is part of pythonOCC.
pythonOCC is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pythonOCC is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.
"""


def get_license_header():
    header = "/*\nCopyright %s %s (%s)\n\n" % (header_year, author, author_email)
    header += license_header
    header += "\n*/\n"
    return header
