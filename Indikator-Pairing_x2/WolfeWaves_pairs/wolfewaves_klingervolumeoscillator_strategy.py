import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_KlingerVolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und KlingerVolumeOscillator
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'KlingerVolumeOscillator': {
                'class': KlingerVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KlingerVolumeOscillator'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'KlingerVolumeOscillator': 1.0
        })
    )
