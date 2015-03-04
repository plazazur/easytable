# The MIT License (MIT)
#
# Copyright (c) 2015 Trung Nguyen <plazazur@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

class EasyTable(object):
    def __init__(self, fields=None, **kwargs):
        self.encoding = kwargs.get("encoding", "UTF-8")

        # Data
        self._fields = []
        if fields:
            self._fields = fields

        self._has_header_printed = False

        self._options = 'vertical_char horizontal_char junction_char'.split()
        for option in self._options:
            if option in kwargs:
                pass
            else:
                kwargs[option] = None

        self._vertical_char = kwargs['vertical_char'] or self._unicode("|")
        self._horizontal_char = kwargs["horizontal_char"] or self._unicode("-")
        self._junction_char = kwargs["junction_char"] or self._unicode("+")

        self._padding = 1

    def _unicode(self, value):
        if not isinstance(value, basestring):
            value = str(value)
        if not isinstance(value, unicode):
            value = unicode(value, self.encoding, "strict")
        return value

    @property
    def vertical_char(self):
        """The charcter used when printing table borders to draw vertical lines

        Arguments:

        vertical_char - single character string used to draw vertical lines"""
        return self._vertical_char
    @vertical_char.setter
    def vertical_char(self, val):
        val = self._unicode(val)
        self._validate_option("vertical_char", val)
        self._vertical_char = val

    @property
    def horizontal_char(self):
        """The charcter used when printing table borders to draw horizontal lines

        Arguments:

        horizontal_char - single character string used to draw horizontal lines"""
        return self._horizontal_char
    @horizontal_char.setter
    def horizontal_char(self, val):
        val = self._unicode(val)
        self._validate_option("horizontal_char", val)
        self._horizontal_char = val

    @property
    def junction_char(self):
        """The charcter used when printing table borders to draw line junctions

        Arguments:

        junction_char - single character string used to draw line junctions"""
        return self._junction_char

    @junction_char.setter
    def junction_char(self, val):
        val = self._unicode(val)
        self._validate_option("vertical_char", val)
        self._junction_char = val


    def add_row(self, row):
        if len(row) != len(self._fields):
            raise Exception('Row should have %d values but has %d values' % (len(self._fields), len(row)))

        if not self._has_header_printed:
            self.print_header()

        self.print_row(row)

    def format_string(self, str, width):
        output = ' ' * self._padding
        if len(str) > width:
            output += str.sub[0: width]
        else:
            output += str + ' ' * (width - len(str) + self._padding)
        output += ' ' * self._padding
        return output

    def print_header(self):
        table_width = 1
        output = self.junction_char
        for field, width in self._fields:
            table_width += width + 2 * self._padding
        output += self.horizontal_char * table_width
        output += self.junction_char
        print(output)

        output = ''
        for field, width in self._fields:
            output += self.vertical_char + self.format_string(field, width)
        output += self.vertical_char
        print(output)


    def print_row(self, row):
        output = ''
        for (value, (name, width)) in zip(row, self._fields):
            output += self.vertical_char + self.format_string(value, width)
        output += self.vertical_char
        print(output)

def main():
    table = EasyTable([('Instance', 10), ('Algorithm', 20)])
    table.add_row(['12', 'strongMIP'])
    table.add_row(['12', 'ejectionChain'])

if __name__ == "__main__":
    main()
