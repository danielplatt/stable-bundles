#!/usr/bin/env python

'''This displays uptime information using uptime. This is redundant,
but it demonstrates expecting for a regular expression that uses subgroups.
PEXPECT LICENSE
    This license is approved by the OSI and FSF as GPL-compatible.
        http://opensource.org/licenses/isc-license.txt
    Copyright (c) 2012, Noah Spurrier <noah@noah.org>
    PERMISSION TO USE, COPY, MODIFY, AND/OR DISTRIBUTE THIS SOFTWARE FOR ANY
    PURPOSE WITH OR WITHOUT FEE IS HEREBY GRANTED, PROVIDED THAT THE ABOVE
    COPYRIGHT NOTICE AND THIS PERMISSION NOTICE APPEAR IN ALL COPIES.
    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
'''

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import pexpect
import re

from pexpect import run

prompt = '/Applications/Magma/magma /Users/daniel/PycharmProjects/stable-bundles/smallPic/testFunc.m x:=5 /Users/daniel/PycharmProjects/stable-bundles/smallPic/testPrint.m'
# out = run(prompt)
# print(out)
#
# exit()


c = pexpect.spawnu(prompt)

c.expect('\w+\r\n')
print(c.after)
c.sendline('1+3;')
c.expect('\w+\r\n')
print(c.after)
