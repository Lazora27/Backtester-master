import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und GannSquares
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'GannSquares': 1.0
        })
    )
