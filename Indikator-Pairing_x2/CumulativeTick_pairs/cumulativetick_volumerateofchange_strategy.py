import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
