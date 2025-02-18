import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'MurreyMathLines': 1.0
        })
    )
