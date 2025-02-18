import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'MurreyMathLines': 1.0
        })
    )
