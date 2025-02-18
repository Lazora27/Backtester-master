import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'MurreyMathLines': 1.0
        })
    )
