from dataclasses import dataclass
from .block import Block

@dataclass
class BlockChain:
    blocks: list
