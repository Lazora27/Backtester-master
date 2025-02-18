import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'HullMovingAverage': 1.0
        })
    )
