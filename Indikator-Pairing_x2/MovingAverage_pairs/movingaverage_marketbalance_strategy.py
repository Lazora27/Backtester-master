import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und MarketBalance
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'MarketBalance': 1.0
        })
    )
