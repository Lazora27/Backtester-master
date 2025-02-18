import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
