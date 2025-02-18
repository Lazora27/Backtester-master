import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeOscillator_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeOscillator und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'VolumeOscillator': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
