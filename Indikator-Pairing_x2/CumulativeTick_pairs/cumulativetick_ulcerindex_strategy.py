import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'UlcerIndex': 1.0
        })
    )
