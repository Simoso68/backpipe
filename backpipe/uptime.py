from time import time
from .builder import BackPipeBuilder

def _uptime(context: BackPipeBuilder):
    return time() - context.started_at