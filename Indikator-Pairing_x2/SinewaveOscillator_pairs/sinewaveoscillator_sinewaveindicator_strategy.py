import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SinewaveOscillator_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SinewaveOscillator und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'SinewaveOscillator': {
                'class': SinewaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SinewaveOscillator'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'SinewaveOscillator': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
