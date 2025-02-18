import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
