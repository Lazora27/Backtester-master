import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KlingerVolumeOscillator_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KlingerVolumeOscillator und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'KlingerVolumeOscillator': {
                'class': KlingerVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KlingerVolumeOscillator'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'KlingerVolumeOscillator': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
