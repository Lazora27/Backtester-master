import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
