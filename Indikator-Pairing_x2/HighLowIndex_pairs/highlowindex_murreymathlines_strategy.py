import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'MurreyMathLines': 1.0
        })
    )
