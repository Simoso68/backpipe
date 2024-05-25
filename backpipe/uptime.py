from time import time
from .builder import BackPipeBuilder

def _uptime(context: BackPipeBuilder) -> float:
    return time() - context.started_at