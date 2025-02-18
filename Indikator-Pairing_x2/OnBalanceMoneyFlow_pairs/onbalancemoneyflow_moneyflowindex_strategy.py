import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceMoneyFlow_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceMoneyFlow und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'OnBalanceMoneyFlow': {
                'class': OnBalanceMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceMoneyFlow'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'OnBalanceMoneyFlow': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
