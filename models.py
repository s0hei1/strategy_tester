from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Candle():
    datetime: datetime
    open : float
    high : float
    low : float
    close : float

@dataclass
class Position:
    entry_price : float
    stop_loss : float
    take_profit : float
    risk : float

@dataclass(frozen=True)
class PositionResult:
    profit : float
