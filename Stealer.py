import base64
import gzip

Blob = b'Enter blob here'
Script = gzip.decompress(base64.b64decode(Blob)).decode()
exec(Script)
