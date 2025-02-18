import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
