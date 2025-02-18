import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
