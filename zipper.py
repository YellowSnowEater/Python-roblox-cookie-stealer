import gzip
import base64

script = r"""Insert script here"""

blob = base64.b64encode(gzip.compress(script.encode()))

print(blob)
