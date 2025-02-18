import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'VolumeOscillator': 1.0
        })
    )
