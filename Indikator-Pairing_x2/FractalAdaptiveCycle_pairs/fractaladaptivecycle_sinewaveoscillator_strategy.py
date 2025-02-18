import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalAdaptiveCycle_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalAdaptiveCycle und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'FractalAdaptiveCycle': {
                'class': FractalAdaptiveCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalAdaptiveCycle'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'FractalAdaptiveCycle': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
