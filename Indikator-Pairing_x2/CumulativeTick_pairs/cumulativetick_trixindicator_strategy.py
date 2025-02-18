import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'TRIXIndicator': 1.0
        })
    )
