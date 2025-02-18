import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
