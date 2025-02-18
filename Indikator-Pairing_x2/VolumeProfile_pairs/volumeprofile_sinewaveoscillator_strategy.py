import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
