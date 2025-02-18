import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'MurreyMathLines': 1.0
        })
    )
