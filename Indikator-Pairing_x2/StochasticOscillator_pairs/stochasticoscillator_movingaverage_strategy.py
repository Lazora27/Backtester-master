import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und MovingAverage
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'MovingAverage': 1.0
        })
    )
