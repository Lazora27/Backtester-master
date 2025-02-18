import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
