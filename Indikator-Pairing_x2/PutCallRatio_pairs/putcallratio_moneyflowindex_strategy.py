import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
