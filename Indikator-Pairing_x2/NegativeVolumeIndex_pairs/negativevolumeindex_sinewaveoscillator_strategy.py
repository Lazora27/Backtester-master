import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
