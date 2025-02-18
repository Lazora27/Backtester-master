import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'MurreyMathLines': 1.0
        })
    )
