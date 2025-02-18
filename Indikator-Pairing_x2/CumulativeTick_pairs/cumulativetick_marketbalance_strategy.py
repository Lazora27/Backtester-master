import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und MarketBalance
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'MarketBalance': 1.0
        })
    )
