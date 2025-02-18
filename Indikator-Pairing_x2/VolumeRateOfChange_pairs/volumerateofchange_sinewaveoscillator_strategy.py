import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeRateOfChange_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeRateOfChange und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'VolumeRateOfChange': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
