import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'MurreyMathLines': 1.0
        })
    )
