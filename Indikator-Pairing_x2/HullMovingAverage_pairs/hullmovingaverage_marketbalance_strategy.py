import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und MarketBalance
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'MarketBalance': 1.0
        })
    )
