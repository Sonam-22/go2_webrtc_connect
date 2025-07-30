import logging
from aioice import Connection
logging.info("Checking aiortc installation")
a = Connection(ice_controlling=False)
b = Connection(ice_controlling=False)
if a.local_username != b.local_username:
  logging.info("aoice installation error.")