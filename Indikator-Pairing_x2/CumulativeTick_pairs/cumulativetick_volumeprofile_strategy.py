import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'VolumeProfile': 1.0
        })
    )
