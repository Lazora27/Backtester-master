import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'VolumeOscillator': 1.0
        })
    )
