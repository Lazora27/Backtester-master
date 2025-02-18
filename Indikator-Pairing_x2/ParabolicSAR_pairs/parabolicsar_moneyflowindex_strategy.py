import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
