import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und DOMDepth
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'DOMDepth': 1.0
        })
    )
