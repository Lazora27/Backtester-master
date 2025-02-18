import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
