import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
