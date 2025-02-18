import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
