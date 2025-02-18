import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'VolumeOscillator': 1.0
        })
    )
