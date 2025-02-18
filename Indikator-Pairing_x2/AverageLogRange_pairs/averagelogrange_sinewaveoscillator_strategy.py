import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
