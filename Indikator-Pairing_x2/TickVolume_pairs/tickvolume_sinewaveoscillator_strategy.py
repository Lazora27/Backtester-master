import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
