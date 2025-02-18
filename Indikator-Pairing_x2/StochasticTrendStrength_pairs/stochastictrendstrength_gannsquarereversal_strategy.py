import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'GannSquareReversal': 1.0
        })
    )
