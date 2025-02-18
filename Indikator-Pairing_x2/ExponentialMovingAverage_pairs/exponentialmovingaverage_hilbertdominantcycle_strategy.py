import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
