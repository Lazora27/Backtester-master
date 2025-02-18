import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
