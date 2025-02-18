import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
