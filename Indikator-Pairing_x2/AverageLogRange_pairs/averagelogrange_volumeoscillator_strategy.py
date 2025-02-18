import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'VolumeOscillator': 1.0
        })
    )
