import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
