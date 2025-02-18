import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und MassIndex
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'MassIndex': 1.0
        })
    )
