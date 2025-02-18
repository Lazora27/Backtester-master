import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeTrendIndicator_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeTrendIndicator und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'VolumeTrendIndicator': 1.0,
            'VolumeOscillator': 1.0
        })
    )
