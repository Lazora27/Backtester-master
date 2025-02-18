import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
