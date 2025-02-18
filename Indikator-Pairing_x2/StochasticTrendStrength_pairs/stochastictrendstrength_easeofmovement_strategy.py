import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'EaseOfMovement': 1.0
        })
    )
