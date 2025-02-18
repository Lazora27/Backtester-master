import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'CumulativeTick': 1.0
        })
    )
