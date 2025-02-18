import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und OpenInterest
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'OpenInterest': 1.0
        })
    )
