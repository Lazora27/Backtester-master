import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'TRIXIndicator': 1.0
        })
    )
