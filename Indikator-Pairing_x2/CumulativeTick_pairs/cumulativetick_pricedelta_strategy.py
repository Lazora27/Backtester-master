import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und PriceDelta
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'PriceDelta': 1.0
        })
    )
