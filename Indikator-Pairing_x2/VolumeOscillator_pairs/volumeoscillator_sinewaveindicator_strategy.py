import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeOscillator_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeOscillator und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'VolumeOscillator': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
