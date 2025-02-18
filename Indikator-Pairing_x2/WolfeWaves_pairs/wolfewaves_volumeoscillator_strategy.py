import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'VolumeOscillator': 1.0
        })
    )
