import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
