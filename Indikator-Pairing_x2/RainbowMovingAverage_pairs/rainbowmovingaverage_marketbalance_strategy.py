import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und MarketBalance
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'MarketBalance': 1.0
        })
    )
