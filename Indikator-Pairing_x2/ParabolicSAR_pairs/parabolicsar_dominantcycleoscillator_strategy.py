import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
