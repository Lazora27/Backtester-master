import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
