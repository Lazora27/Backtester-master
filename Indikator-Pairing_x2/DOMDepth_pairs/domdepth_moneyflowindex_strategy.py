import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
