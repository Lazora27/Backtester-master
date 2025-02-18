import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
