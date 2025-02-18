import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
