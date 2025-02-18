import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'VolumeOscillator': 1.0
        })
    )
