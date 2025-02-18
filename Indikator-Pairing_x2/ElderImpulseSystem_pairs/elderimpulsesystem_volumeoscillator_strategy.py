import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'VolumeOscillator': 1.0
        })
    )
