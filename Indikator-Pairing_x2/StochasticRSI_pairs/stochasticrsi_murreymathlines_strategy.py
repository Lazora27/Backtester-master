import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'MurreyMathLines': 1.0
        })
    )
