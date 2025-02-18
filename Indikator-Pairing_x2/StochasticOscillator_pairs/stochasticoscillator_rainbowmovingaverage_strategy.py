import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
