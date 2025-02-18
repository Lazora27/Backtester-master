import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
