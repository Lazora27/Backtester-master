import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und MarketBalance
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'MarketBalance': 1.0
        })
    )
