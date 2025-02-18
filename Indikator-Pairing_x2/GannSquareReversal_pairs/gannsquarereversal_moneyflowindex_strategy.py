import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
