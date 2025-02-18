import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'CumulativeTick': 1.0
        })
    )
