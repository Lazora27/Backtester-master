import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeOscillator_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeOscillator und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'VolumeOscillator': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
