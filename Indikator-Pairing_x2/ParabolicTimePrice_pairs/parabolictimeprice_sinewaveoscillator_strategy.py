import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicTimePrice_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicTimePrice und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'ParabolicTimePrice': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
