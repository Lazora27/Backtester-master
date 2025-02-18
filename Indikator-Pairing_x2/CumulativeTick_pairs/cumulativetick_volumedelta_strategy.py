import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'VolumeDelta': 1.0
        })
    )
