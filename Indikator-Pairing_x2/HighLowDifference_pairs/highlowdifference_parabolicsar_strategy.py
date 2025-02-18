import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'ParabolicSAR': 1.0
        })
    )
