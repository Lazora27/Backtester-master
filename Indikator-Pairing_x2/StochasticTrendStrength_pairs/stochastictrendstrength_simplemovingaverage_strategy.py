import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
