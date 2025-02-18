import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'ParabolicSAR': 1.0
        })
    )
