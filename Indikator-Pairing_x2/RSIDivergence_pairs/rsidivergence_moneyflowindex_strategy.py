import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
