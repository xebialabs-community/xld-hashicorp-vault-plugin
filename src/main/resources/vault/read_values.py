#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import hvac
import sys

# Using plaintext
vault_server = target.vaultServer
print "Connection to client {0} {1}".format(vault_server.name, vault_server.url)
client = hvac.Client(url=vault_server.url, token=vault_server.rootToken)
if target.vaultKey is None:
    key = "secret/{0}".format(target.id)
else:
    key = target.vaultKey
print 'the vault key is {0}'.format(key)
read_values = client.read(key)
if read_values is None:
    print "Key {0} not found".format(key)
    sys.exit(1)

for k in read_values['data']:
    v = read_values['data'][k]
    print "overide {0} property".format(k)
    target.setProperty(k, v)
