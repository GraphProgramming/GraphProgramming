from typing import Callable
from gpm.pyGP.registry import register
NODES = {}

@register(NODES,
    name="Example Str Concat",
    inputs=dict(inp="String"),
    outputs=dict(outp="String"))
def init(global_state, text: str = "Hello World") -> Callable:
    """
    Limit the FPS throughput.
    """
    def tick(inp):
        return {"outp": inp + text}
    return tick
