import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und MarketBalance
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'MarketBalance': 1.0
        })
    )
