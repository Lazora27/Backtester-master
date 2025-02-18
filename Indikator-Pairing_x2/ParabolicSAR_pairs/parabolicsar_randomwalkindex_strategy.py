import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
