import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und TrueRange
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'TrueRange': 1.0
        })
    )
