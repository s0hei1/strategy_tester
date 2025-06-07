from numpy.random.mtrand import Sequence
from typing import ForwardRef
from models import Candle

StrategyTester = ForwardRef("StrategyTester")

class StrategyTester():


    def __init__(self, candlestick_chart_data : Sequence[Candle], positions : Sequence[Position]):
        pass

    def test(self):
        pass





    @classmethod
    def from_csv(cls) -> StrategyTester:
        pass
