from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import pexpect
import re

from pexpect import run
from pexpect.exceptions import TIMEOUT

example_as_list = [
    'q1<t>:=PolynomialRing(RationalField());',
    'z4<x,y,z,w>:=PolynomialRing(IntegerRing(),4);',
    'f:=x^4+x^3*z+x^2*y^2+x^2*y*w+x^2*z^2+x^2*z*w+x*y^3+x*y*z*w+x*y*w^2+x*z^2*w+y^3*w+y^2*z^2+y^2*z*w+y^2*w^2+y*z^2*w+z^4+z*w^3;',
    'p:=2;'
]
# prompt = '/Applications/Magma/magma /Users/daniel/PycharmProjects/stable-bundles/smallPic/PicNumberModp.m '+example+' /Users/daniel/PycharmProjects/stable-bundles/smallPic/runPic.m'
# print(prompt)


c = pexpect.spawnu('/Applications/Magma/magma /Users/daniel/PycharmProjects/stable-bundles/smallPic/PicNumberModp.m')
c.expect('Loading file')
c.expect('>')

for comm in example_as_list:
    c.sendline(comm)
    c.expect('>')
    # print('%s ---- %s ---- %s' % (comm, c.before, c.after))

# c.expect('\w+\r\n')
# print(c.after)
# c.sendline(example)
# print('sending important line')
c.expect('>')
c.sendline('<PicNumberModp(f,p),998+1>;')
# print('waiting for line result')
# print(c.readline())
c.expect('999')
# print('be:%s----af:%s' %(c.before,c.after))
print(c.before)

exit()

try:
    c.expect('\w+\r\n', timeout=40)
except TIMEOUT:
    print(c.before)
    print(c.after)
print(c.after)

exit()

out = run(prompt)
print(out)

exit()

c = pexpect.spawnu(prompt)
# c.expect('>')
# c.sendline('1+3;')
c.expect('\w+\r\n', timeout=60)
print(c.before)
print(c.after)
