import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und OpenInterest
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'OpenInterest': 1.0
        })
    )
