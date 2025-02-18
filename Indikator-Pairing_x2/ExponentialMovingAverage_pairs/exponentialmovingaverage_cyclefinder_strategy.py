import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und CycleFinder
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'CycleFinder': 1.0
        })
    )
