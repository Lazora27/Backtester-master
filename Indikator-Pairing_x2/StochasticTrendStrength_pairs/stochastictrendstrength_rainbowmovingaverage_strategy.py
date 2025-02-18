import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
