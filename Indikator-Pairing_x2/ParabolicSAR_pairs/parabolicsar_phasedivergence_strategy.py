import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'PhaseDivergence': 1.0
        })
    )
