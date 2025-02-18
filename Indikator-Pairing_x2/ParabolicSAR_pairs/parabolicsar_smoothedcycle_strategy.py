import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'SmoothedCycle': 1.0
        })
    )
